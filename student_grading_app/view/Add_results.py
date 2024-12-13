import tkinter

import customtkinter
from customtkinter import *
from student_grading_app.controllers import Admin_control
from tkinter import Canvas
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

from student_grading_app.models import Admin,Course

PRIMARY_COLOR = "#3B82F6"  # Blue
SECONDARY_COLOR = "#F3F4F6"  # Light Gray
ACCENT_COLOR = "#10B981"  # Green
TEXT_COLOR = "#1F2937"  # Dark Gray
BACKGROUND_COLOR = "#FFFFFF"  # White
plus_image = None


class Add_students_results(CTk):
    def __init__(self):
        super().__init__()

        self.AdminModel = Admin.AdminModel()
        self.CourseModel=Course.CourseModel()
        global plus_image  # the use of global her was an attempt to solve the pyimage5 problem but
        self.plus_image = plus_image
        set_appearance_mode("dark")

        self.title("New Results")
        self.geometry("300x400")  # Adjusted size to fit the image and frame properly
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.configure(fg_color="blue")
        # level selection deliberately decided to deal with it out of the db bcs the levels are known and constant
        #IN DEFINING THIS VARIABLE DUE TO TIME CONSTRINTS, I INVOLUNTARILY CALLED MY MODEL FUNCTION DIRECTLY WITHOUT PASSING THROUGH CONTROL🙏🏾
        # dropdown atrributes
        self.levels = ["level 1", "level 2", "level 3", "level 4"]
        self.selected_level = customtkinter.StringVar(value=self.levels[0])
        self.course = self.CourseModel.fetch_course_from_name()
        self.selected_courses = customtkinter.StringVar(value=self.course[0] if self.course else "")

        # image handeling
        self.plus_image = Image.open("C:/Users/Tab's/PycharmProjects/SGApp/IMG/plus.gif").resize((600, 500))
        self.plus_image_tk = ImageTk.PhotoImage(self.plus_image)

        self.canvas = Canvas(self, width=500, height=350)
        self.canvas.pack(anchor="nw", fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.plus_image_tk, anchor="nw")

        self.entry_frame = CTkFrame(self, fg_color="transparent")
        self.entry_frame_window = self.canvas.create_window(200, 250, window=self.entry_frame)  # Adjusted positioning

        #self.course_name_entry = CTkEntry(self.entry_frame, width=200, placeholder_text="Course")
        #self.course_name_entry.grid(padx=10, pady=(10, 20))

        #course dropdown

        self.course_menu = customtkinter.CTkOptionMenu(self.entry_frame, variable=self.selected_courses,
                                                       values=self.course,
                                                       fg_color="#333333", width=200, button_color=PRIMARY_COLOR,
                                                       button_hover_color=ACCENT_COLOR,
                                                       dropdown_fg_color="#B5B2B3",
                                                       dropdown_hover_color=SECONDARY_COLOR,
                                                       dropdown_text_color=TEXT_COLOR)
        self.course_menu.grid(padx=10, pady=(10, 20))
        self.course_code_entry = CTkEntry(self.entry_frame, width=200, placeholder_text="Course_code")
        self.course_code_entry.grid(padx=10, pady=(10, 20))
        # level Dropdown
        self.level_menu = customtkinter.CTkOptionMenu(self.entry_frame, variable=self.selected_level,
                                                      values=self.levels,
                                                      fg_color="#333333", width=200, button_color=PRIMARY_COLOR,
                                                      button_hover_color=ACCENT_COLOR,
                                                      dropdown_fg_color="#B5B2B3",
                                                      dropdown_hover_color=SECONDARY_COLOR,
                                                      dropdown_text_color=TEXT_COLOR)
        self.level_menu.grid(padx=10, pady=(10, 20))

        self.semester_entry = CTkEntry(self.entry_frame, width=200, placeholder_text="Semester")
        self.semester_entry.grid(padx=10, pady=(10, 20))

        self.add_entry = CTkEntry(self.entry_frame, width=200, height=50, placeholder_text="Select File",
                                  fg_color="#333333", corner_radius=5, border_width=5, border_color="black")
        self.add_entry.grid(pady=10, padx=20)
        self.add_button = CTkButton(self.entry_frame, text="Select File", fg_color="#333333", corner_radius=5,
                                    border_width=5, border_color="#333333", command=self.select_file)
        self.add_button.grid(pady=10, padx=20)  # Added padding for better spacing

        self.add_button = CTkButton(self.entry_frame, text="Add", fg_color="#333333", width=45, height=45)
        self.add_button.grid(pady=20, padx=20, sticky="e")  # Added padding for better spacing

    def select_file(self):
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        entry_field = self.add_entry
        entry_field.delete(0, customtkinter.END)
        entry_field.insert(0, path)
        self.extract_file()

    def extract_file(self):
        path = self.add_entry.get()
        read_file = Admin_control.read_csv(path)
        extract_file = Admin_control.extract_marks(read_file)


if __name__ == "__main__":
    Page = Add_students_results()
    Page.mainloop()
