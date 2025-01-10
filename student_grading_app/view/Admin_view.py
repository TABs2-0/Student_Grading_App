import os

import customtkinter
from tkinter import Canvas
from student_grading_app.view import Add_results
import customtkinter as ctk
from student_grading_app.controllers import Admin_control, Course_control, Student_control
import tkinter as tk
from PIL import Image, ImageTk
from customtkinter import CTkLabel, CTkComboBox, CTkCanvas, CTkFrame, CTk
from tkinter import ttk

#QEEN's WORK, Still have to connect our two ui's


# Initialize CustomTkinter
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")

# Colors from Figma design
PRIMARY_COLOR = "#3B82F6"  # Blue
SECONDARY_COLOR = "#F3F4F6"  # Light Gray
ACCENT_COLOR = "#10B981"  # Green
TEXT_COLOR = "#1F2937"  # Dark Gray
BACKGROUND_COLOR = "#FFFFFF"  # White


class AdminDashboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Admin Dashboard")
        self.C = Course_control.CourseControl()
        self.Grades = Student_control.StudentControl()
        self.A = Admin_control.AdminControl()
        self.geometry("1000x700")
        self.configure(fg_color=BACKGROUND_COLOR)

        # Data

        # Define a dictionary to store course data
        #self.course_data = {
        ##      "lecturer": "Mr. John Smith",  # Lecturer's name
        #     "code": "STAT101",  # Course code
        #       "students": [  # List of students enrolled in the course
        #          {"name": "John Ode", "mat": "ICTU2021333E", "caScore": 30, "examScore": 50},  # Student 1
        #         {"name": "No 2", "mat": "ICTU2021333E", "caScore": 30, "examScore": 10},  # Student 2
        #    ],
        #},
        #"Comp Org": {  # Course name
        #   "lecturer": "Dr. Jane Doe",  # Lecturer's name
        #  "code": "COMP201",  # Course code
        # "students": [  # List of students enrolled in the course
        #    {"name": "Mayt", "mat": "ICTU2021333E", "caScore": 30, "examScore": 50},  # Student 1
        #   {"name": "Sam 2", "mat": "ICTU2021333E", "caScore": 30, "examScore": 10},  # Student 2
        #],
        #},
        #"Data Structures": {  # Course name
        #   "lecturer": "Prof. Alan Turing",  # Lecturer's name
        #  "code": "COMP301",  # Course code
        # "students": [  # List of students enrolled in the course
        #    {"name": "Alice", "mat": "ICTU2021456A", "caScore": 40, "examScore": 45},  # Student 1
        #   {"name": "Bob", "mat": "ICTU2021789B", "caScore": 35, "examScore": 50},  # Student 2
        #],
        #},
        #"Operating Systems": {  # Course name
        #   "lecturer": "Dr. Grace Hopper",  # Lecturer's name
        #  "code": "COMP401",  # Course code
        # "students": [  # List of students enrolled in the course
        #    {"name": "Charlie", "mat": "ICTU2021234C", "caScore": 25, "examScore": 35},  # Student 1
        #   {"name": "Dana", "mat": "ICTU2021567D", "caScore": 40, "examScore": 40},  # Student 2
        #],
        #},
        #}

        self.selected_course = ctk.StringVar(value="Prob and Stat")
        self.build_ui()

    def build_ui(self):
        # Main frame
        main_frame = ctk.CTkFrame(self, fg_color=BACKGROUND_COLOR)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Title
        title_label = ctk.CTkLabel(main_frame, text="Admin Dashboard", font=("Arial", 28, "bold"),
                                   text_color=PRIMARY_COLOR)
        title_label.pack(pady=20)

        # Course Selector
        course_frame = ctk.CTkFrame(main_frame, fg_color=SECONDARY_COLOR, corner_radius=10)
        course_frame.pack(fill="x", padx=20, pady=10)

        course_label = ctk.CTkLabel(course_frame, text="Select Course:", font=("Arial", 16), text_color=TEXT_COLOR)
        course_label.pack(side="left", padx=10, pady=10)

        course_names = self.C.fetch_courses_from_name_control()  #
        self.selected_course.set(course_names[0] if course_names else "")  #

        course_menu = ctk.CTkOptionMenu(course_frame, values=course_names,
                                        variable=self.selected_course, command=self.update_course_display,
                                        fg_color=PRIMARY_COLOR, button_color=PRIMARY_COLOR,
                                        button_hover_color=ACCENT_COLOR,
                                        dropdown_fg_color=BACKGROUND_COLOR, dropdown_hover_color=SECONDARY_COLOR,
                                        dropdown_text_color=TEXT_COLOR)
        course_menu.pack(side="left", padx=10, pady=10)

        # Lecturer and Course Code
        self.info_frame = ctk.CTkFrame(main_frame, fg_color=SECONDARY_COLOR, corner_radius=10)
        self.info_frame.pack(fill="x", padx=20, pady=10)
        self.lecturer_label = ctk.CTkLabel(self.info_frame, text="Lecturer: ", font=("Arial", 16),
                                           text_color=TEXT_COLOR)
        self.lecturer_label.pack(side="left", padx=10, pady=10)
        self.code_label = ctk.CTkLabel(self.info_frame, text="Course Code: ", font=("Arial", 16), text_color=TEXT_COLOR)
        self.code_label.pack(side="left", padx=10, pady=10)

        # Table
        table_frame = ctk.CTkFrame(main_frame, fg_color=SECONDARY_COLOR, corner_radius=10)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree = ttk.Treeview(table_frame,
                                 columns=("Name", "Mat", "CA Score", "Exam Score", "Final Score", "Grade", "Credit"),
                                 show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Mat", text="Mat")
        self.tree.heading("CA Score", text="CA Score")
        self.tree.heading("Exam Score", text="Exam Score")
        self.tree.heading("Final Score", text="Final Score")
        self.tree.heading("Grade", text="Grade")
        self.tree.heading("Credit", text="Credit")
        self.tree.pack(pady=10, padx=10, fill="both", expand=True)

        # Customize Treeview colors
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background=BACKGROUND_COLOR, foreground=TEXT_COLOR, rowheight=25,
                        fieldbackground=BACKGROUND_COLOR)
        style.map('Treeview', background=[('selected', ACCENT_COLOR)])
        style.configure("Treeview.Heading", background=PRIMARY_COLOR, foreground=BACKGROUND_COLOR, relief="flat")
        style.map("Treeview.Heading", background=[('active', ACCENT_COLOR)])

        # Add Student Button
        add_button = ctk.CTkButton(main_frame, text="Add Student", fg_color=ACCENT_COLOR, hover_color=PRIMARY_COLOR,
                                   command=self.open_add_student_form)
        add_button.pack(pady=20)

        self.update_course_display()

    def update_course_display(self, *args):
        course_name = self.selected_course.get()
        course_info = self.C.fetch_courses_from_control(course_name)  #
        if course_info:
            course_name, course_code, lecturer_name = course_info

            # Update Lecturer and Course Code
            self.lecturer_label.configure(text=f"Lecturer: {lecturer_name}")
            self.code_label.configure(text=f"Course Code: {course_code}")

            # Update Table
            for row in self.tree.get_children():
                self.tree.delete(row)

            students = self.Grades.get_grades_from_control(course_code)  #
            for student in students:
                final_score = self.A.calculate_final_score(student[2], student[3])  #
                grade, credit = self.A.calculate_grade(final_score)
                self.tree.insert("", "end", values=(
                    student[0],
                    student[1],
                    student[2],
                    student[3],
                    final_score,
                    grade,
                    f"{credit:.1f}"))  #

    def open_add_student_form(self):
        form_window = ctk.CTkToplevel(self)
        form_window.title("Add Student")
        form_window.geometry("400x500")
        form_window.configure(fg_color=BACKGROUND_COLOR)

        ctk.CTkLabel(form_window, text="Add Student", font=("Arial", 24, "bold"), text_color=PRIMARY_COLOR).pack(
            pady=20)

        fields = [
            ("Grade_id", "grade_id"),
            ("Matriculation Number", "mat"),
            ("Course_code", "course_code"),
            ("CA Score", "ca"),
            ("Exam Score", "exam")
        ]

        entries = {}
        for field_name, field_id in fields:
            frame = ctk.CTkFrame(form_window, fg_color=SECONDARY_COLOR, corner_radius=10)
            frame.pack(fill="x", padx=20, pady=10)
            ctk.CTkLabel(frame, text=f"{field_name}:", font=("Arial", 14), text_color=TEXT_COLOR).pack(side="left",
                                                                                                       padx=10, pady=5)
            entry = ctk.CTkEntry(frame, fg_color=BACKGROUND_COLOR, text_color=TEXT_COLOR, corner_radius=5)
            entry.pack(side="right", padx=10, pady=5, fill="x", expand=True)
            entries[field_id] = entry

        course_frame = ctk.CTkFrame(form_window, fg_color=SECONDARY_COLOR, corner_radius=10)
        course_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(course_frame, text="Course:", font=("Arial", 14), text_color=TEXT_COLOR).pack(side="left", padx=10,
                                                                                                   pady=5)
        course_var = ctk.StringVar(value=list(self.C.fetch_courses_from_name_control())[0])  #
        course_menu = ctk.CTkOptionMenu(course_frame, variable=course_var,
                                        values=self.C.fetch_courses_from_name_control(),
                                        fg_color=PRIMARY_COLOR, button_color=PRIMARY_COLOR,
                                        button_hover_color=ACCENT_COLOR,
                                        dropdown_fg_color=BACKGROUND_COLOR, dropdown_hover_color=SECONDARY_COLOR,
                                        dropdown_text_color=TEXT_COLOR)
        course_menu.pack(side="right", padx=10, pady=5, fill="x", expand=True)

        def submit():
            course = course_var.get()
            try:
                #understand whats hapenning here
                new_student = {
                    "grade_id": entries["grade_id"].get(),
                    "mat": entries["mat"].get(),
                    "course_code": entries["course_code"].get(),
                    "caScore": int(entries["ca"].get()),
                    "examScore": int(entries["exam"].get())

                }
                self.Grades.add_grades_from_control(new_student["grade_id"], new_student["mat"],
                                                    new_student["course_code"],
                                                    new_student["caScore"], new_student["examScore"])
                self.update_course_display()
                form_window.destroy()
            except ValueError:
                error_label = ctk.CTkLabel(form_window, text="Invalid input. Please check your entries.",
                                           text_color="red")
                error_label.pack(pady=10)
                form_window.after(3000, error_label.destroy)

        submit_button = ctk.CTkButton(form_window, text="Submit", fg_color=ACCENT_COLOR, hover_color=PRIMARY_COLOR,
                                      command=submit)
        submit_button.pack(pady=20)


class Adminhome(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.current_index = 0
        Levels = ["Level One", "Level Two", "Level Three", "Level Four"]
        ctk.set_appearance_mode("dark")
        self.title("Admin_Page")
        self.geometry("750x750")
        semesters = ["Fall", "Spring", "Summer"]
        #self.resizable(False, False)

        # Background Image
        self._image = Image.open(
            "C:/Users/Tab's/PycharmProjects/SGApp/IMG/pexels-karolina-grabowska-5477714.jpg").resize(
            (2000, 1000))
        self._photo = ImageTk.PhotoImage(self._image, size=(10, 30))

        # Create a canvas to hold the background image
        self.canvas = Canvas(self, width=750, height=750)
        self.canvas.grid(row=0, column=0, rowspan=10, columnspan=10, sticky="nsew")
        self.canvas.create_image(0, 0, image=self._photo, anchor="center")
        self.image_reference = self._photo  # to try solve thy Pyimage notfound by pointing towards it

        # Navigation for other widgets like "My Account"
        self.Nav_1 = ctk.CTkLabel(master=self.canvas, width=10, height=20, text="")
        self.Nav_1.grid(row=0, column=100, columnspan=10, sticky="nsew")

        self.MyAccount_IMG_1 = ctk.CTkImage(
            light_image=Image.open("C:/Users/Tab's/PycharmProjects/SGApp/IMG/myaccount.png"), size=(30, 30))
        self.account_button = ctk.CTkButton(master=self.Nav_1, image=self.MyAccount_IMG_1, text="My Account",
                                            corner_radius=5)
        self.account_button.grid(row=0, column=0, padx=10, sticky="w")

        self.add_result_button = ctk.CTkButton(master=self.Nav_1, image=self.MyAccount_IMG_1, text="Submit Result",
                                               corner_radius=5, command=self.display_add_course)
        self.add_result_button.grid(row=0, column=0, padx=10, sticky="n")

        self.Logout_IMG_2 = ctk.CTkImage(Image.open("C:/Users/Tab's/PycharmProjects/SGApp/IMG/5528144.png"))
        self.button_background_image = ctk.CTkImage(
            Image.open("C:/Users/Tab's/PycharmProjects/SGApp/IMG/Button_Background-Images.jpg"))
        self.log_out__button = ctk.CTkButton(master=self.Nav_1, image=self.Logout_IMG_2, corner_radius=5,
                                             text="Log_Out", command=self.logout)
        self.log_out__button.grid(row=0, column=0, padx=10, sticky="e")

        self.text = "                                                         "  # Home page text
        self.Nav = ctk.CTkLabel(master=self.Nav_1, width=10, height=20, anchor="center", font=("Retro cool", 24),
                                text=self.text, text_color="black")
        self.Nav.grid(row=1, column=0, padx=10, sticky="nsew")
        self.animate_text(0)

        # Frame for the semester buttons display
        self.frame_0 = ctk.CTkFrame(master=self, width=200, height=700, fg_color="#000080")  # Blue
        self.frame_0.grid(row=2, column=9, rowspan=8, padx=10, pady=50, sticky="ne")

        # Frame for the level display
        self.frame = ctk.CTkFrame(master=self, width=300, height=700, fg_color="#000080")  # Blue
        self.frame.grid(row=2, column=0, rowspan=8, padx=10, pady=50, sticky="sw")

        self.frame_1 = ctk.CTkFrame(master=self.frame, width=200, height=700, fg_color="#000080")
        self.frame_1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        for j in range(4):
            self.level = ctk.CTkLabel(master=self.frame_1, fg_color="grey", text=Levels[j], font=("Arial", 12))
            self.level.grid(row=j, column=100, pady=75, sticky="n")

        for i in range(4):
            self.frame_2 = ctk.CTkFrame(master=self.frame_0, width=200, height=700, fg_color="#FF7F50")  # Orange Frame
            self.frame_2.grid(row=i, column=100, padx=10, pady=20, sticky="nsew")

            for semester in semesters:
                List = ctk.CTkButton(master=self.frame_2, width=100, height=100, fg_color="#000080", text=semester,
                                     font=("Roboto", 15), image=self.button_background_image,
                                     command=self.display_a_course_result)
                List.grid(row=0, column=semesters.index(semester), pady=5, padx=5)

    # the function below is the to apply the animation
    def animate_text(self, index):

        max_index = len(self.text) - 1
        if index < len(self.text):
            self.Nav.configure(text=self.Nav.cget("text") + self.text[self.current_index])
            self.current_index += 1
            self.after(15, self.animate_text, index + 1)
        else:
            pass

    # the function below will be modified to consider the level and semesters from the db
    def display_a_course_result(self):
        self.withdraw()

        app = AdminDashboardApp()
        app.mainloop()

    def display_add_course(self):
        self.withdraw()

        add_result = Add_results.Add_students_results()
        add_result.mainloop()

    def logout(self):
        self.destroy()


if __name__ == "__main__":
    A = Adminhome()
    A.mainloop()
