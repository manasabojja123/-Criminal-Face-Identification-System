from tkinter import *
import shutil
from PIL import ImageTk, Image
import sqlite3
from tkinter import filedialog
import tkinter.messagebox as tmsg
import cv2
from subprocess import call

def callTrainer():
    call(["python", "trainer1.py"])

def registerNew():
    def saveNew():
        # Get the user input
        name = Fullname.get()
        # Other fields...

        # Validate the input
        if not name:
            tmsg.showerror("Error", "Name field cannot be empty")
            return

        # Create a new folder for the individual
        new_folder_path = os.path.join("images", name)
        os.makedirs(new_folder_path)

        # Copy the selected image to the new folder
        if file1:
            shutil.copy(file1, os.path.join(new_folder_path, "1.png"))
        else:
            tmsg.showerror("Error", "Please select an image")

        # Add the individual's information to the database
        conn = sqlite3.connect('criminal.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO People (Name) VALUES (?)', (name,))
        conn.commit()
        conn.close()

        tmsg.showinfo("Success", "New individual registered successfully")
        root_new.destroy()

    root_new = Toplevel()
    root_new.geometry('500x300')
    root_new.title("Register New Individual")

    Fullname = StringVar()

    label_0 = Label(root_new, text="Register New Individual", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)

    label_1 = Label(root_new, text="Name:", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)

    entry_1 = Entry(root_new, textvar=Fullname)
    entry_1.place(x=240, y=130)

    Button(root_new, text='Select Image', width=20, bg='brown', fg='white', command=mfileopen).place(x=180, y=180)
    Button(root_new, text='Save', width=20, bg='brown', fg='white', command=saveNew).place(x=180, y=230)

def appendExisting():
    def selectExisting():
        # Get the selected individual's name
        name = var.get()

        # Copy the selected image to the individual's folder
        if name:
            selected_folder = os.path.join("images", name)
            if file1:
                shutil.copy(file1, os.path.join(selected_folder, "new_image.png"))
                tmsg.showinfo("Success", "Image appended to existing individual successfully")
                root_existing.destroy()
            else:
                tmsg.showerror("Error", "Please select an image")
        else:
            tmsg.showerror("Error", "Please select an individual")

    root_existing = Toplevel()
    root_existing.geometry('500x300')
    root_existing.title("Append to Existing Individual")

    var = StringVar()

    label_0 = Label(root_existing, text="Append to Existing Individual", width=20, font=("bold", 20))
    label_0.place(x=50, y=53)

    label_1 = Label(root_existing, text="Select Individual:", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)

    # Fetch existing individuals from the database
    conn = sqlite3.connect('criminal.db')
    cursor = conn.cursor()
    cursor.execute('SELECT Name FROM People')
    rows = cursor.fetchall()
    conn.close()

    names = [row[0] for row in rows]

    option_menu = OptionMenu(root_existing, var, *names)
    option_menu.place(x=240, y=130)

    Button(root_existing, text='Select Image', width=20, bg='brown', fg='white', command=mfileopen).place(x=180, y=180)
    Button(root_existing, text='Append', width=20, bg='brown', fg='white', command=selectExisting).place(x=180, y=230)

def mfileopen():
    global file1
    file1 = filedialog.askopenfilename()

root = Tk()
root.geometry('1350x720')
root.minsize(1350,720)
root.state("zoomed")
root.title("CFIS- Criminal Face Identification System")

label_0 = Label(root, text="Advanced Criminal Identification System", width=85, height=1, font=("bold", 20), anchor='center', bg="#386184", fg="white")
label_0.place(x=0, y=105)

label_1 = Label(root, text="Registration Form", width=115, font=("bold", 16), bg="#180020", fg='white')
label_1.place(x=0, y=42)

Button(root, text='Register New Individual', width=20, font=("bold",10), bg='brown', height=2, fg='white', command=registerNew).place(x=100, y=180)
Button(root, text='Append to Existing Individual', width=20, font=("bold",10), bg='brown', height=2, fg='white', command=appendExisting).place(x=300, y=180)

root.mainloop()
