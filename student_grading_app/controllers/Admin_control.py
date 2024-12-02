#import customtkinter
#import PIL
import customtkinter
from customtkinter import *


class StudentInfo(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("750*750")
        self.title("student information")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.resizable(False,False)
        self.label_matricule = customtkinter.CTkLabel(self, text="Matricule: ICT20241132")

        self.label_matricule.pack(pady=10)

        self.label_name = customtkinter.CTkLabel(self, text="Name: TWYLA")
        self.label_name.pack(pady=15)

        self.label_grade = customtkinter.CTkLabel(self, text="Grade: A")
        self.label_grade.pack(pady=20)


studentinfo = StudentInfo()
studentinfo.mainloop()