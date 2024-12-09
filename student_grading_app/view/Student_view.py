#import customtkinter
from PIL import Image, ImageTk
import customtkinter
import tkinter as tk
from customtkinter import *

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
        self.background_photo = ImageTk.PhotoImage( self.background_image, size=(10, 30))
        self.canvas = tk.Canvas(self, width=200, height=250)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(130, 130, image=self.background_photo, anchor="w")

        self.label_welcome = customtkinter.CTkLabel(self, text="Hey Anelle  you have come a long way ‼️,Congrats",
                                                    font=("Arial", 25))  # after db creation ,this text should

        self.label_welcome.pack(pady=10)

        for course in courses:
            self.label_grade = customtkinter.CTkLabel(self, text=f"{course} ", fg_color="blue",
                                                      corner_radius=10)
            self.label_grade.pack(pady=20)


studentinfo = StudentValidatedCourses()
studentinfo.mainloop()
