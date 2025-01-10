import customtkinter
import customtkinter as ctk
from tkinter import messagebox, filedialog
from student_grading_app.controllers import Lecturer_control
from PIL import Image, ImageTk
import sqlite3
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importing Image and ImageTk from PIL
from student_grading_app.view import Add_results, login


class LecturerLogin(tk.Tk):
    def __init__(self,lecturer_name):#THE NAME HERE IS TO KEEP TRACK OF  WHICH LECTURER IS ACCESSING THE PAGE
        super().__init__()

        self.title("Lecturer Home Page")
        self.geometry('900x700')  # Increased height for better layout
        self.configure(background="#1E90FF")# blue
        self.LecturerControl = Lecturer_control.LecturerControl()
        self.lecturer_name=lecturer_name
        self.setup_ui()

    import tkinter as tk
    import customtkinter as ctk
    from PIL import Image, ImageTk

    def setup_ui(self):
        # Frame for course list
        self.course_frame = tk.Frame(self, bg="#1F2937")
        self.course_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Load the background image
        self.background_image = Image.open(
            "C:/Users/Tab's/PycharmProjects/SGApp/IMG/pexels-karolina-grabowska-5477714.jpg")
        self.background_image = self.background_image.resize((900, 700))  # Resize to fit the window
        self.bg_image = ImageTk.PhotoImage(self.background_image)

        # Create a label to hold the background image
        self.background_label = tk.Label(self.course_frame, image=self.bg_image)
        self.background_label.place(relwidth=1, relheight=1)  # Make the label fill the window

        # Create label for course list title
        self.course_title_label = tk.Label(self.course_frame, text=f"{self.lecturer_name} Lets Wrapp On Your Courses", font=("Arial", 16, "bold"),
                                           bg="#1F2937", fg="#8A2BE2")
        self.course_title_label.pack(pady=10)

        # Create list of courses
        #self.course_list = ["PROGRAMMING IN PYTHON", "COMPUTER ORGANIZATION", "TECHNICAL WRITING", "JAVA PROGRAMMING",
         #                   "INTRODUCTION TO SOFTWARE", "PROBABILITY AND STATISTICS"]

        #replacing dictionary with DB
        self.course_list=self.LecturerControl.get_lecturer_courses(self.lecturer_name)

        # Create listbox for courses
        self.course_listbox = tk.Listbox(self.course_frame, width=50, height=10, fg="white", bg="#3B4252",
                                         selectbackground="#8A2BE2", font=("Arial", 12))
        for course in self.course_list:
            self.course_listbox.insert(tk.END, course)
        self.course_listbox.pack(pady=10, padx=20)

        # Create upload entry and button
        self.add_entry = ctk.CTkEntry(self.course_frame, width=200, height=50, placeholder_text="Select File",
                                      font=("Arial", 16, "bold"),
                                      bg_color="#1F2937", fg_color="black",placeholder_text_color="#8A2BE2")
        self.add_entry.pack(pady=10)

        self.upload_button = ctk.CTkButton(self.course_frame, text="Upload", width=200, height=50,
                                           command=self.select_file, fg_color="black", hover_color="#88C0D0",text_color='#8A2BE2',
                                           corner_radius=10)
        self.upload_button.pack(pady=10)

    def select_file(self):
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        entry_field = self.add_entry
        entry_field.delete(0, customtkinter.END)
        entry_field.insert(0, path)

    def send_csv_file(self):# to send csv results  rigth now
        pass


if __name__ == "__main__":
    app = LecturerLogin("John Smith")
    app.mainloop()
