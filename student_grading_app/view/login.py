import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import tkinter as tk
from student_grading_app import view
from student_grading_app import models
from student_grading_app.models.User import UserModel


class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")

        self.title("Login Page")
        self.geometry("600x400")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.background_image = Image.open("C:/Users/Tab's/OneDrive/Desktop/customTkinter/login_img.jpg").resize(
            (750, 750))
        self.background_photo = ImageTk.PhotoImage(self.background_image, size=(10, 30))

        # Create a canvas to hold the background image
        self.canvas = tk.Canvas(self, width=100, height=400)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        self.frame = ctk.CTkFrame(self, bg_color="transparent")  # Transparent background
        self.frame.grid(row=0, column=0, padx=20, pady=20)

        # image label
        self.welcome_label = ctk.CTkLabel(self.frame, text="Welcome to YrApp!", font=("Arial", 18, "bold"),
                                          text_color="white")
        self.welcome_label.pack(pady=(20, 10))

        self.username_entry = ctk.CTkEntry(self.frame, width=200, placeholder_text="Username")
        self.username_entry.pack(pady=(10, 10))

        self.password_entry = ctk.CTkEntry(self.frame, width=200, show="*", placeholder_text="Password")
        self.password_entry.pack(pady=(10, 20))

        #login and signin buttons
        self.login_button = ctk.CTkButton(self.frame, border_color="#A45EE5", fg_color="#A45EE5", text="Login",
                                          command=self.authentify)

        self.login_button.pack(pady=10)

        self.signin_button = ctk.CTkButton(self.frame, border_color="#A45EE5", fg_color="#A45EE5", text="Sign In")
        self.signin_button.pack(pady=10)

    def authentify(self):

        userName = self.username_entry.get()  # this stores the entry data
        password = self.password_entry.get()

        user = UserModel.Fetchuserrole( UserModel,userName, password)  #fetch  the user name and password which coresponds
        if user:
            role = user[0]
            if userName == '' and password == '':
                tk.messagebox.showwarning('Fill in the form first')

            elif role == "Admin":
                log = Login()
                log.withdraw()

                admin_home = view.Admin_view.Adminhome()
                admin_home.mainloop()
            elif role == "lecturer":
                log = Login()
                log.withdraw()

                lecturer_home = view.Lecturer_view.LectureView()
                lecturer_home.mainloop()
            elif role == "student":
                log = Login()
                log.withdraw()
                student_home = view.Student_view.StudentValidatedCourses()
                student_home.mainloop()
            else:
                tk.messagebox.showerror('Invalid Entries')


login = Login()
login.mainloop()

#this is normally within the class
