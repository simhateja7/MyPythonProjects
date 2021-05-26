from tkinter import *

from tkinter import filedialog

from PIL import Image,ImageTk


root=Tk()

root.title("ImageConversion")
root.iconbitmap("C:\\Users\\simha\\OneDrive\\Desktop\\GUI_tkinter\\logo.ico")
root.geometry("500x650")
root.configure(bg="#1b1b21")

def pngTojpg():
    global picture

    for item in frame.winfo_children():
        item.destroy()
    root.filename=filedialog.askopenfilename(title="choose a picture",filetypes=(("png files","*.png"),("all types","*.*")))
    if root.filename!="":
        png_pic=Image.open(root.filename)
        r_png=png_pic.resize((450,500),Image.ANTIALIAS)
        picture=ImageTk.PhotoImage(r_png)

        lab=Label(frame,image=picture)
        lab.pack()
        if ent.get() == '':
            lab.destroy()
            error=Label(root,text="enter your file name please",fg="red",padx=40)
            error.grid(row=3,column=0,columnspan=2)
        else:
            with open((root.filename),"rb") as pic:
                b_pic=pic.read()
            with open((ent.get()+".jpg"),"wb") as new_pic:
                jpg_pic=new_pic.write(b_pic)

            save=Label(root,text="your picture converted and saved successfully",fg="green",padx=40)
            save.grid(row=3,column=0,columnspan=2)
def jpgTOpng():
    global picture1

    for item in frame.winfo_children():
        item.destroy()
    root.filename=filedialog.askopenfilename(title="choose a picture",filetypes=(("jpeg files","*.jpeg"),("all types","*.*")))
    if root.filename!="":
        jpg_pic=Image.open(root.filename)
        r_jpg=jpg_pic.resize((450,500),Image.ANTIALIAS)
        picture1=ImageTk.PhotoImage(r_jpg)

        lab=Label(frame,image=picture1)
        lab.pack()
        if ent.get() == '':
            lab.destroy()
            error=Label(root,text="enter your file name please",fg="red",padx=40)
            error.grid(row=3,column=0,columnspan=2)
        else:
            with open((root.filename),"rb") as pic:
                b_pic=pic.read()
            with open((ent.get()+".png"),"wb") as new_pic:
                png_pic=new_pic.write(b_pic)

            save=Label(root,text="your picture converted and saved successfully",fg="green",padx=40)
            save.grid(row=3,column=0,columnspan=2)

def clear():
    for item in frame.winfo_children():
        item.destroy()
    ent.delete(0,end)


frame=Frame(root,width=450,height=550)
#create the button
pngTojpg=Button(root,text="PNGtoJPG",padx=20,pady=7,font="none 12 bold",command=pngTojpg)
clear=Button(root,text="clear",padx=20,pady=7,font="noen 12 bold",command=clear)
jpgTOpng=Button(root,text="JPGtoPNG",padx=20,pady=7,font="none 12 bold",command=jpgTOpng)
lab=Label(root,text="File Name",font="none 12",bg="#1b1b21")
ent=Entry(root,font="none 12 bold")

frame.grid(row=0,column=0,columnspan=3,padx=27,pady=(2,5))
pngTojpg.grid(row=1,column=0)
clear.grid(row=1,column=1)
jpgTOpng.grid(row=1,column=2)
lab.grid(row=2,column=0,pady=(20,0))
ent.grid(row=2,column=1,pady=(20,0))
root.mainloop()
