import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import tkinter as tk

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importing Image and ImageTk from PIL


class LecturerLogin(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lecturer Login")
        self.geometry("400x500")  # Increased height for better layout

        self.setup_ui()

    def setup_ui(self):
        # Frame for course list
        self.course_frame = tk.Frame(self, bg="#ADD8E6")
        self.course_frame.pack(pady=20)

        # Load the background image
        background_image = Image.open(
            "C:/Users/Tab's/PycharmProjects/SGApp/IMG/pexels-karolina-grabowska-5477714.jpg")  # Replace with your image path
        background_image = background_image.resize((400, 500))  # Resize to fit the window
        self.bg_image = ImageTk.PhotoImage(background_image)

        # Create a label to hold the background image
        self.background_label = tk.Label(self.course_frame, image=self.bg_image,height=400,width=500)
        self.background_label.place(relwidth=1, relheight=1)  # Make the label fill the window

        # Create label for course list title
        self.course_title_label = tk.Label(self.course_frame, text="Course List", font=("Arial", 12, "bold"), bg="#ADD8E6")
        self.course_title_label.pack()

        # Create list of courses
        self.course_list = ["PROGRAMMING IN PYTHON", "COMPUTER ORGANIZATION", "TECHNICAL WRITING", "JAVA PROGRAMMING",
                            "INTRODUCTION TO SOFTWARE", "PROBABILITY AND STATISTICS"]

        # Create listbox for courses
        self.course_listbox = tk.Listbox(self.course_frame, width=50, height=10, justify='center')  # Centered text
        for course in self.course_list:
            self.course_listbox.insert(tk.END, course)
        self.course_listbox.pack(pady=10)

        # Create upload button
        self.upload_button = tk.Button(self.course_frame, text="Upload", width=10, command=self.upload)
        self.upload_button.pack(pady=10)

    def upload(self):
        messagebox.showinfo("Upload", "Upload functionality not implemented yet.")


if __name__ == "__main__":
    app = LecturerLogin()
    app.mainloop()
