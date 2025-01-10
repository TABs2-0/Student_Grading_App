import tkinter
import customtkinter
from customtkinter import *
from student_grading_app.controllers import Admin_control, Course_control, Student_control
from student_grading_app.view import Admin_view
from tkinter import Canvas, filedialog
from PIL import Image, ImageTk
import pandas as pd

from student_grading_app.models import Admin, Course, Student

PRIMARY_COLOR = "#3B82F6"
SECONDARY_COLOR = "#F3F4F6"
ACCENT_COLOR = "#10B981"
TEXT_COLOR = "#1F2937"
BACKGROUND_COLOR = "#FFFFFF"


class Add_students_results(CTk):
    def __init__(self):
        super().__init__()

        # Initialize controllers and models
        self.AdminModel = Admin.AdminModel()
        self.StudentControl = Student_control.StudentControl()
        self.CourseModel = Course.CourseModel()
        self.CourseControl = Course_control.CourseControl()
        self.Grades = Student_control.StudentControl()
        self.AdminView = Admin_view.AdminDashboardApp()
        self.StudentModel = Student.StudentModel()
        self.AdminControl = Admin_control.AdminControl()

        # Instance variables
        self.complete_file = pd.DataFrame()
        self.csv_path = None

        set_appearance_mode("dark")

        # Window setup
        self.title("New Results")
        self.geometry("300x400")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.configure(fg_color="blue")

        # Initialize dropdown data
        self.levels = ["level 1", "level 2", "level 3", "level 4"]
        self.selected_level = customtkinter.StringVar(value=self.levels[0])
        self.course = self.CourseModel.fetch_course_from_name()
        self.selected_courses = customtkinter.StringVar(value=self.course[0] if self.course else "")

        self.setup_ui()

    def setup_ui(self):
        # Image handling
        try:
            self.plus_image = Image.open("C:/Users/Tab's/PycharmProjects/SGApp/IMG/plus.gif").resize((600, 500))
            self.plus_image_tk = ImageTk.PhotoImage(self.plus_image)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.plus_image_tk = None

        # Canvas setup
        self.canvas = Canvas(self, width=500, height=350)
        self.canvas.pack(anchor="nw", fill="both", expand=True)
        if self.plus_image_tk:
            self.canvas.create_image(0, 0, image=self.plus_image_tk, anchor="nw")

        # Entry frame setup
        self.entry_frame = CTkFrame(self, fg_color="transparent")
        self.entry_frame_window = self.canvas.create_window(200, 250, window=self.entry_frame)

        # Course dropdown
        self.course_menu = customtkinter.CTkOptionMenu(
            self.entry_frame,
            variable=self.selected_courses,
            values=self.course,
            fg_color="#333333",
            width=200,
            button_color=PRIMARY_COLOR,
            button_hover_color=ACCENT_COLOR,
            dropdown_fg_color="#B5B2B3",
            dropdown_hover_color=SECONDARY_COLOR,
            dropdown_text_color=TEXT_COLOR
        )
        self.course_menu.grid(padx=10, pady=(10, 20))

        # Course code entry
        self.course_code_entry = CTkEntry(self.entry_frame, width=200, placeholder_text="Course_code")
        self.course_code_entry.grid(padx=10, pady=(10, 20))

        # Level dropdown
        self.level_menu = customtkinter.CTkOptionMenu(
            self.entry_frame,
            variable=self.selected_level,
            values=self.levels,
            fg_color="#333333",
            width=200,
            button_color=PRIMARY_COLOR,
            button_hover_color=ACCENT_COLOR,
            dropdown_fg_color="#B5B2B3",
            dropdown_hover_color=SECONDARY_COLOR,
            dropdown_text_color=TEXT_COLOR
        )
        self.level_menu.grid(padx=10, pady=(10, 20))

        # Semester entry
        self.semester_entry = CTkEntry(self.entry_frame, width=200, placeholder_text="Semester")
        self.semester_entry.grid(padx=10, pady=(10, 20))

        # File selection
        self.add_entry = CTkEntry(
            self.entry_frame,
            width=200,
            height=50,
            placeholder_text="Select File",
            fg_color="#333333",
            corner_radius=5,
            border_width=5,
            border_color="black"
        )
        self.add_entry.grid(pady=10, padx=20)

        # Buttons
        self.select_button = CTkButton(
            self.entry_frame,
            text="Select File",
            fg_color="#333333",
            corner_radius=5,
            border_width=5,
            border_color="#333333",
            command=self.select_file
        )
        self.select_button.grid(pady=10, padx=20)

        self.add_button = CTkButton(
            self.entry_frame,
            text="Add",
            fg_color="#333333",
            width=45,
            height=45,
            command=self.submit_from_csv
        )
        self.add_button.grid(pady=20, padx=20, sticky="e")

    def select_file(self):
        """Handle file selection and load CSV data"""
        self.csv_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.csv_path:
            self.add_entry.delete(0, customtkinter.END)
            self.add_entry.insert(0, self.csv_path)
            try:
                self.complete_file = self.AdminControl.main_csv_marks(self.csv_path)
            except Exception as e:
                self.show_error(f"Error loading CSV file: {str(e)}")

    def update_course_display_from_csv(self):
        """Update the course display with CSV data"""
        if not self.complete_file:
            self.show_error("No CSV file loaded")
            return

        try:
            self.course_name = self.selected_courses.get()
            self.course_info = self.CourseControl.fetch_courses_from_control(self.course_name)

            if self.course_info:
                self.course_name, course_code, lecturer_name = self.course_info

                # Update labels
                self.AdminView.lecturer_label.configure(text=f"Lecturer: {lecturer_name}")
                self.AdminView.code_label.configure(text=f"Course Code: {course_code}")

                # Clear existing table
                for row in self.AdminView.tree.get_children():
                    self.AdminView.tree.delete(row)

                # Update table with new data
                for _, row in self.complete_file.iterrows():
                    matricule = self.StudentControl.get_matricule_from_student_id(row["StudentID"])
                    self.AdminView.tree.insert("", "end", values=(
                        row["Name"],
                        matricule,
                        row["CAScore"],
                        row["ExamScore"],
                        row["FinalScore"],
                        row["Grade"],
                        row["Credits"],
                        f"{float(row['Credits']):.1f}"
                    ))
        except Exception as e:
            self.show_error(f"Error updating display: {str(e)}")

    def submit_from_csv(self):

        if self.complete_file.empty:
            self.show_error("No CSV file loaded")
            return

        try:
            for _, row in self.complete_file.iterrows():# iterate through the DataFrame
                matricule = self.StudentControl.get_matricule_from_student_id(row["StudentID"])
                self.Grades.add_grades_from_control(
                    row["GradeID"],
                    matricule,
                    self.course_code_entry.get(),
                    row["CAScore"],
                    row["ExamScore"],
                    row["FinalScore"],
                    row["Grade"],
                    row["Credits"]
                )
            self.update_course_display_from_csv()
            self.destroy()
        except Exception as e:
            self.show_error(f"Error submitting grades: {str(e)}")

    def show_error(self, message):

        error_label = customtkinter.CTkLabel(self, text=message, text_color="red")
        error_label.pack(pady=10)
        self.after(3000, error_label.destroy)


if __name__ == "__main__":
    Page = Add_students_results()
    Page.mainloop()
