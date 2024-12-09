import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import tkinter as tk


class LectureView(ctk.CTk):
    import tkinter as tk

    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.title("Lecture Page")

        # Create the main window

        self.title("Teacher's Dashboard")
        self.geometry("300x350")  # Adjust window size as needed

        self.configure(bg="#F0F0F0")  # Set background color

        # Create the teacher name label and entry field
        self.teacher_name_label = ctk.CTkLabel(self, text="Welcome Back  ENGR ANDREW AGBOR", text_color="black",bg_color="#ADD8E6",fg_color="#ADD8E6", font=("Arial", 12))
        self.teacher_name_label.pack(pady=10)  # Add padding



        # Create the courses label
        self.courses_label = ctk.CTkLabel(self, text="Courses You Already Uploaded", bg_color="#F08080", font=("Arial", 14, "bold"))
        self.courses_label.pack(pady=10)  # Add padding

        # Create the course buttons
        course_buttons = [
            ctk.CTkButton(self, text="Real Analysis 1           Level1--Fall--2024", bg_color="#ADD8E6", width=20, height=2, font=("Arial", 12)),
            ctk.CTkButton(self, text="Computing in Society       Level1--Fall--2024",bg_color="#ADD8E6", width=20, height=2, font=("Arial", 12)),
            ctk.CTkButton(self, text="Probability and Statistics  Level2--Fall--2024", bg_color="#ADD8E6", width=20, height=2, font=("Arial", 12))
        ]

        for button in course_buttons:
            button.pack(pady=5)  # Add padding between buttons

        # Create the upload button
        upload_button = ctk.CTkButton(self, text="Upload", command=upload_button_clicked, bg_color="#808080",
                                      font=("Arial", 12))
        upload_button.pack(pady=10)


def upload_button_clicked():
    # Add your upload functionality here
    print("Upload button clicked!")


lecturer = LectureView()
lecturer.mainloop()
