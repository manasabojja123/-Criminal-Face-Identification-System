from tkinter import *
import shutil
from PIL import ImageTk, Image
import sqlite3
from tkinter import filedialog
import tkinter.messagebox as tmsg
from subprocess import call
from tkinter import font


def register():
    call(["python", "registerGUI1.py"])
def VideoSurveillance():
    call(["python", "survi1.py"])
def detectCriminal():
    call(["python", "detect.py"])


root = Tk()
#Modified
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f'{screen_width}x{screen_height}')
root.minsize(screen_width, screen_height)
root.maxsize(screen_width, screen_height)

#root.geometry('800x500')
#root.minsize(800,500)
#root.maxsize(800,500)

root.title("Advanced Criminal Identification System")
root.configure(bg="#382273")


Fullname=StringVar()
father=StringVar()
var = IntVar()
c=StringVar()
d=StringVar()
var1= IntVar()
file1=""
image=Image.open("image.jpg")
photo=ImageTk.PhotoImage(image)
photo_label=Label(image=photo,width=1300,height=0,bg='white').place(x=0,y=0)
photo_label


label_0 = Label(root, text="Advanced Criminal Identification System",width=82,height=1,font=("bold", 20),anchor='center',bg="#386184",fg="white")
label_0.place(x=0,y=105)

#Modified

Button(root, text='REGISTER CRIMINAL',width=35,height=3,bg='blue',fg='white',font=("bold", 11),command=register).place(x=490,y=190)
Button(root, text='PHOTO MATCH',width=35,height=3,bg='blue',fg='white',font=("bold", 11),command=detectCriminal).place(x=490,y=270)
Button(root, text='VIDEO SURVEILLANCE',width=35,height=3,bg='red',fg='white',font=("bold", 11),command=VideoSurveillance).place(x=490,y=350)

#Button(root, text='REGISTER CRIMINAL',width=35,height=3,bg='blue',fg='white',font=("bold", 11),command=register).place(x=250,y=180)
#Button(root, text='PHOTO MATCH',width=35,height=3,bg='blue',fg='white',font=("bold", 11),command=detectCriminal).place(x=250,y=260)
#Button(root, text='VIDEO SURVEILLANCE',width=35,height=3,bg='red',fg='white',font=("bold", 11),command=VideoSurveillance).place(x=250,y=340)

root.mainloop()
