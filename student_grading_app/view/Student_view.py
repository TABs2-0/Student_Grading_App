#import customtkinter
from tkinter import ttk

from PIL import Image, ImageTk

import customtkinter
import tkinter as tk
from customtkinter import *


#By Rodia
class EnrolledCourses(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('900x700')
        self.title('Enrolled Courses')
        customtkinter.set_appearance_mode("dark")
        self.configure(bg="#537198")
        self.label = customtkinter.CTkLabel(self, text='ALL COURSES', font=('Arial', 20, 'bold'))
        self.label.pack(pady=10)
        self.entry = customtkinter.CTkEntry(
            self, placeholder_text="Search Enrolled Courses Here", width=300)
        self.entry.pack(pady=10)
        self.frame = customtkinter.CTkFrame(self, width=300, corner_radius=10, fg_color="blue")
        self.frame.pack(pady=10, padx=20, side="left", anchor="nw")
        self.label_name = customtkinter.CTkLabel(
            self.frame, text="STUDENT NAME: RODIA", font=('Arial', 14, 'bold'))
        self.label_name.pack(pady=5, padx=10)

        self.label_matricule = customtkinter.CTkLabel(
            self.frame, text="STUDENT MATRICULE: ICTU2023", font=('Arial', 14, 'bold'))
        self.label_matricule.pack(pady=5, padx=10)

        self.label_enrol = customtkinter.CTkLabel(
            self, text='📚 Enrolled Courses', font=('Arial', 17, 'bold'))
        self.label_enrol.pack(pady=80, anchor="w")
        self.table_frame = customtkinter.CTkFrame(self, fg_color="#537198")
        self.table_frame.pack(pady=90, padx=50, fill="both", expand=True)

        self.table = ttk.Treeview(
            self.table_frame,
            columns=('COURSES', 'COURSE ID', 'CREDIT', 'STATUS'),
            show='headings',
            height=2,
        )
        self.table.heading('COURSES', text='COURSES')
        self.table.heading('COURSE ID', text='COURSE ID')
        self.table.heading('CREDIT', text='CREDIT')
        self.table.heading('STATUS', text='STATUS')

        self.table.column('COURSES', anchor='center', width=150)
        self.table.column('COURSE ID', anchor='center', width=50)
        self.table.column('CREDIT', anchor='center', width=25)
        self.table.column('STATUS', anchor='center', width=100)

        self.table.pack(fill="both", expand=True)
        courses = [
            ('PROBABILITY', 'ICT2110', '4', 'REQUIREMENT'),
            ('COMPUTER ORGANISATION', 'ICT2130', '4', 'REQUIREMENT'),
            ('PROGRAMMING IN PYTHON', 'ICT2113', '4', 'COMPULSORY'),
            ('JAVA PROGRAMMING', 'ICT2002', '4', 'COMPULSORY'),
            ('TECHNICAL WRITING', 'ICT2003', '4', 'COMPULSORY'),
            ('INTRO TO SOFTWARE', 'ICT2140', '4', 'COMPULSORY'),
        ]

        for course in courses:
            self.table.insert('', 'end', values=course)


courses = ["Real Analysis 2 :            A", "Algorithm and Datastructure2:           A",
           "linear Algebra:              D", "Discrete Math:           C", "OOP:             B"]


class StudentValidatedCourses(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.geometry("600*400")
        self.title("student Course Record")

        self.background_image = Image.open("C:/Users/Tab's/PycharmProjects/SGApp/IMG/Old-School-Image (1).png").resize(
            (400, 400))
        self.background_photo = ImageTk.PhotoImage(self.background_image, size=(10, 30))
        self.canvas = tk.Canvas(self, width=200, height=250)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(130, 130, image=self.background_photo, anchor="w")

        self.label_welcome = customtkinter.CTkLabel(self, text="Hey Anelle  you have come a long way ‼️,Congrats",
                                                    font=("Arial", 25))  # after db creation ,this text should

        self.label_welcome.pack(pady=10)
        self.past_course = customtkinter.CTkButton(self, border_color="#A45EE5", fg_color="#A45EE5", text="What U Did",
                                                   command=self.display)
        self.past_course.pack(pady=10,anchor="s")
        for course in courses:
            self.label_grade = customtkinter.CTkLabel(self, text=f"{course} ", fg_color="blue",
                                                      corner_radius=10)
            self.label_grade.pack(pady=20)

    import customtkinter
    from tkinter import ttk

    def display(self):
        self.withdraw()

        enrolled_courses = EnrolledCourses()
        enrolled_courses.mainloop()


studentinfo = StudentValidatedCourses()
studentinfo.mainloop()
