from customtkinter import *
from tkinter import Canvas
from PIL import Image, ImageTk
import tkinter as tk


class Add_students_results(CTk):
    def __init__(self):
        super().__init__()
        set_appearance_mode("dark")

        self.title("New Results")
        self.geometry("300x400")  # Adjusted size to fit the image and frame properly
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.configure(fg_color="pink")

        self.plus_image = Image.open("C:/Users/Tab's/PycharmProjects/SGApp/IMG/plus.jpg").resize((600, 500))
        self.plus_image_tk = ImageTk.PhotoImage(self.plus_image)

        self.canvas = Canvas(self, width=500, height=350)
        self.canvas.pack(anchor="nw", fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.plus_image_tk, anchor="nw")

        self.entry_frame = CTkFrame(self, fg_color="transparent")
        self.entry_frame_window = self.canvas.create_window(200, 250, window=self.entry_frame)  # Adjusted positioning

        self.course_name_entry = CTkEntry(self.entry_frame, width=200, placeholder_text="Course")
        self.course_name_entry.grid(padx=10,pady=(10,20))
        self.course_code_entry = CTkEntry(self.entry_frame, width=200, placeholder_text="Course_code")
        self.course_code_entry.grid(padx=10,pady=(10,20))
        self.semester_entry = CTkEntry(self.entry_frame, width=200, placeholder_text="Semester")
        self.semester_entry.grid(padx=10,pady=(10,20))
        self.Level_entry = CTkEntry(self.entry_frame, width=200, placeholder_text="Level")
        self.Level_entry.grid(padx=10,pady=(10,20))
        self.add_button = CTkButton(self.entry_frame, text="Select File", fg_color="black",corner_radius=5,border_width=5,border_color="black")
        self.add_button.grid(pady=20, padx=20)  # Added padding for better spacing

        self.add_button = CTkButton(self.entry_frame, text="Add",fg_color="black",width=45,height=45)
        self.add_button.grid(pady=20, padx=20,sticky="e")  # Added padding for better spacing


if __name__ == "__main__":
    Page = Add_students_results()
    Page.mainloop()
