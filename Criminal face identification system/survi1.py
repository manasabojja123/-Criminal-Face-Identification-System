import cv2
import numpy as np
import sqlite3
import face_recognition as fr
import numpy as np
from tkinter import *
from tkinter import ttk
import os
import imutils
import math
import winsound
from PIL import Image, ImageTk

class App:
    def __init__(self, video_source):
        self.appname = "CFIS- Criminal Face Identification System"
        self.window = Tk()
        self.window.title(self.appname)
        self.window.geometry('1350x720')
        self.window.state("zoomed")
        self.window["bg"] = '#382273'
        self.video_source = video_source
        self.vid = MyVideoCapture(self.video_source)
        self.label = Label(self.window, text=self.appname, font=("bold", 20), bg='blue', fg='white')
        self.label.pack(side=TOP, fill=BOTH)
        self.canvas = Canvas(self.window, height=700, width=700, bg='#382273')
        self.canvas.pack(side=LEFT, fill=BOTH)
        self.detected_people = []
        self.images = self.load_images_from_folder("images")

        self.image_names = []
        for img in self.images:
            self.image_names.append(fr.load_image_file(os.path.join("images", img)))

        self.encodings = []
        for img in self.image_names:
            self.encodings.append(fr.face_encodings(img)[0])

        self.known_face_names = []
        for name in self.images:
            self.known_face_names.append((os.path.splitext(name)[0]).split('.')[1])

        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True

        print(self.known_face_names)
        
        self.tree = ttk.Treeview(self.window, column=("column1", "column2", "column3", "column4", "column5"),
                                  show='headings')

        self.tree.heading("#1", text="Cr-ID")
        self.tree.column("#1", minwidth=0, width=70, stretch=NO)

        self.tree.heading("#2", text="NAME")
        self.tree.column("#2", minwidth=0, width=200, stretch=NO)

        self.tree.heading("#3", text="CRIME")
        self.tree.column("#3", minwidth=0, width=150, stretch=NO)

        self.tree.heading("#4", text="Nationality")
        self.tree.column("#4", minwidth=0, width=100, stretch=NO)

        self.tree.heading("#5", text="MATCHING %")
        self.tree.column("#5", minwidth=0, width=120, stretch=NO)

        ttk.Style().configure("Treeview.Heading", font=('Calibri', 13, 'bold'), foreground="red", relief="flat")

        self.tree.place(x=710, y=50)
        # self.tree.bind("<Double-1>", self.double_click)

        self.update()
        self.window.mainloop()

    def load_images_from_folder(self, folder):
        images = []
        for filename in os.listdir(folder):
            images.append(filename)
        return images
    
    def double_click(self, event):
        item = self.tree.selection()
        itemid = self.tree.item(item, "values")
        ide = itemid[0]
        ide = int(ide)
        self.view_detail(ide)
        
    def view_detail(self, a):
        conn = sqlite3.connect("criminal.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM people where Id=" + str(a))
        rows = cur.fetchall()
        print(rows)
        for row in rows:
            label_n = Label(self.window, text=row[1], bg="#382273", fg='white', width=20, font=("bold", 12)) 
            label_n.place(x=1123,y=400)
            label_f = Label(self.window, text=row[3], bg="#382273", fg='white', width=20, font=("bold", 12))
            label_f.place(x=1123, y=430)
            label_m = Label(self.window, text=row[4], bg="#382273", fg='white', width=20, font=("bold", 12)) 
            label_m.place(x=1123,y=460)
            label_g = Label(self.window, text=row[2], bg="#382273", fg='white', width=20, font=("bold", 12))
            label_g.place (x=1123,y=490)
            label_r = Label(self.window, text=row[5], bg="#382273", fg='white', width=20, font=("bold", 12)) 
            label_r.place(x=1123,y=520)
            label_bl = Label(self.window, text=row[6], bg="#382273", fg='white', width=20, font=("bold", 12))
            label_bl.place(x=1123,y=550)
            label_b = Label(self.window, text=row[7], bg="#382273", fg='white', width=20, font=("bold", 12))
            label_b.place(x=1123,y=580)
            label_n = Label(self.window, text=row[8], bg="#382273", fg='white', width=20, font=("bold", 12)) 
            label_n.place(x=1123,y=610)
            label_c = Label(self.window, text=row[9], width=20, bg="#382273", font=("bold", 12), fg='white')
            label_c.place(x=1123,y=640)
        conn.close()
        label_name = Label(self.window, text="Name", bg="#382273", fg='yellow', width=20, font=("bold", 12)) 
        label_name.place(x=930,y=400)
        label_father = Label(self.window, text="FatherName", bg="#382273", fg='yellow', width=20, font=("bold", 12)) 
        label_father.place(x=930,y=430)
        label_mother = Label(self.window, text="MotherName", bg="#382273", fg='yellow', width=20, font=("bold", 12))
        label_mother.place(x=930,y=460)
        label_gender = Label(self.window, text="Gender", bg="#382273", fg='yellow', width=20, font=("bold", 12)) 
        label_gender.place(x=930,y=490)
        label_religion = Label(self.window, text="Religion", bg="#382273", fg='yellow', width=20, font=("bold", 12)) 
        label_religion.place(x=930,y=520)
        label_bloodgroup = Label(self.window, text="Blood Group", bg="#382273", fg='yellow', width=20, font=("bold", 12))
        label_bloodgroup.place(x=930,y=550)
        label_body = Label(self.window, text="BodyMark", bg="#382273", fg='yellow', width=20, font=("bold", 12))
        label_body.place(x=930,y=580)
        label_nat = Label(self.window, text="Nationality", bg="#382273", fg='yellow', width=20, font=("bold", 12))
        label_nat.place(x=930,y=610)
        label_crime = Label(self.window, text="Crime", bg="#382273", width=20, font=("bold", 12), fg='yellow')
        label_crime.place(x=930,y=640)

        x = 'user.' + str(a) + ".png"
        image = Image.open('images/'+ x)
        image = image.resize((180, 180), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        photo_l = Label(image=photo, width=180, height=180)
        photo_l.place(x=750,y=450).pack()

    # def update(self):
    #     if self.vid:
    #         ret, frame = self.vid.get_frame()
    #         if ret:
    #             self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
    #             self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

    #             # Resize the frame of video to 1/4 size for fast process
    #             small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    #             # Convert the image to BGR color (OpenCV) to RGB color (face_recognition)
    #             rgb_small_frame = small_frame[:, :, ::-1]

    #             # Only process every other frame of video to save time
    #             # (Skipping processing every frame to increase performance)
    #             if self.process_this_frame:
    #                 # Find all the faces and face encodings in the current frame of video
    #                 self.face_locations = fr.face_locations(rgb_small_frame)
    #                 self.face_encodings = fr.face_encodings(rgb_small_frame, self.face_locations)
    #                 self.face_names = []

    #                 for face_encoding in self.face_encodings:
    #                     # See if the face is a match for known face(s)
    #                     matches = fr.compare_faces(self.encodings, face_encoding)
    #                     Id = 0
    #                     face_distances = fr.face_distance(self.encodings, face_encoding)
    #                     best_match_index = np.argmin(face_distances)

    #                     percent = self.show_percentage_match(face_distances[best_match_index])

    #                     if matches[best_match_index]:
    #                         Id = self.known_face_names[best_match_index]
    #                     self.face_names.append(Id)

    #                     profile = self.get_profile(Id)
    #                     confidence = str(round(percent * 100, 2)) + "%"

    #                     if profile not in self.detected_people and profile is not None:
    #                         self.detected_people.append(profile)
    #                         profilex = list(profile)
    #                         profilex.append(confidence)
    #                         profile = tuple(profilex)
    #                         self.tree.insert("", 'end', values=profile)
    #                         winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

    #                 # Printing the detected profiles for debugging
    #                 print(profile)

    #     self.window.after(15, self.update)
    def update(self):
    #   if profile is not None:
    #     percent = str(round(percent * 100, 2)) + "%"  # Moved from earlier in the code
    #     confidence = percent  # Define confidence based on percent
    #     if profile not in self.detected_people:
    #         self.detected_people.append(profile)
    #         profilex = list(profile)
    #         profilex.append(confidence)
    #         profile = tuple(profilex)
    #         self.tree.insert("", 'end', values=profile)
    #         self.tree.bind("<Double-1>", self.double_click)
    #         winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

        if self.vid:
                ret, frame = self.vid.get_frame()
                if ret:
                    self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                    self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

                    # Resize the frame of video to 1/4 size for fast process
                    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                    # Convert the image to BGR color (OpenCV) to RGB color (face_recognition)
                    rgb_small_frame = small_frame[:, :, ::-1]

                    # Only process every other frame of video to save time
                    # (Skipping processing every frame to increase performance)
                    if self.process_this_frame:
                        # Find all the faces and face encodings in the current frame of video
                        self.face_locations = fr.face_locations(rgb_small_frame)
                        self.face_encodings = fr.face_encodings(rgb_small_frame, self.face_locations)
                        self.face_names = []

                        for face_encoding in self.face_encodings:
                            # See if the face is a match for known face(s)
                            matches = fr.compare_faces(self.encodings, face_encoding)
                            Id = 0
                            face_distances = fr.face_distance(self.encodings, face_encoding)
                            best_match_index = np.argmin(face_distances)

                            percent = self.show_percentage_match(face_distances[best_match_index])

                            if matches[best_match_index]:
                                Id = self.known_face_names[best_match_index]
                            self.face_names.append(Id)

                            profile = self.get_profile(Id)
                            if profile is not None:
                                confidence = str(round(percent * 100, 2)) + "%"
                                if profile not in self.detected_people:
                                    self.detected_people.append(profile)
                                    profilex = list(profile)
                                    profilex.append(confidence)
                                    profile = tuple(profilex)
                                    self.tree.insert("", 'end', values=profile)
                                    self.tree.bind("<Double-1>",self.double_click)
                                    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

                        # Printing the detected profiles for debugging
                            print(profile)

        self.window.after(15, self.update)
           


    def show_percentage_match(self, face_distance):
        # Function to calculate the percentage match based on distance
        face_match_threshold = 0.6  # Example threshold, you can adjust this
        if face_distance > face_match_threshold:
            range_val = (1.0 - face_match_threshold)
            linear_val = (1.0 - face_distance) / (range_val * 2.0)
            return linear_val
        else:
            range_val = face_match_threshold
            linear_val = 1.0 - (face_distance / (range_val * 2.0))
            return linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))

    def get_profile(self, id):
        # Function to retrieve profile from database based on ID
        conn = sqlite3.connect("criminal.db")
        cur = conn.cursor()
        # cur.execute("SELECT * FROM people WHERE Id=?", (id,))
        cur.execute("SELECT ID,name,crime,nationality FROM people where ID="+str(id))
        profile = cur.fetchone()
        conn.close()
        return profile


       

class MyVideoCapture:
    def __init__(self, video_source):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            frame = imutils.resize(frame, height=700)
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


if __name__ == "__main__":
    video_source = 0  # Webcam
    App(video_source)
    
