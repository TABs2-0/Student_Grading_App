import customtkinter as ctk
from tkinter import ttk

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
        self.geometry("1000x700")
        self.configure(fg_color=BACKGROUND_COLOR)

        # Data
        self.course_data = {
            "Prob and Stat": {
                "lecturer": "Mr. John Smith",
                "code": "STAT201",
                "students": [
                    {"name": "John Ode", "mat": "ICTU2021333E", "caScore": 30, "examScore": 50},
                    {"name": "No 2", "mat": "ICTU2021333E", "caScore": 30, "examScore": 10},
                ],
            },
            "Comp Org": {
                "lecturer": "Dr. Jane Doe",
                "code": "COMP101",
                "students": [
                    {"name": "Mayt", "mat": "ICTU2021333E", "caScore": 30, "examScore": 50},
                    {"name": "Sam 2", "mat": "ICTU2021333E", "caScore": 30, "examScore": 10},
                ],
            },
            "Data Structures 1": {
                "lecturer": "Prof. Alan Turing",
                "code": "DS101",
                "students": [
                    {"name": "Alice", "mat": "ICTU2021456A", "caScore": 40, "examScore": 45},
                    {"name": "Bob", "mat": "ICTU2021789B", "caScore": 35, "examScore": 50},
                ],
            },
            "Operating Systems": {
                "lecturer": "Dr. Grace Hopper",
                "code": "OS401",
                "students": [
                    {"name": "Charlie", "mat": "ICTU2021234C", "caScore": 25, "examScore": 35},
                    {"name": "Dana", "mat": "ICTU2021567D", "caScore": 40, "examScore": 40},
                ],
            },
        }

        self.selected_course = ctk.StringVar(value="Prob and Stat")
        self.build_ui()

# this function  will display the ui
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

        course_menu = ctk.CTkOptionMenu(course_frame, values=list(self.course_data.keys()),
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

        # Table to display the students mark
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

    def calculate_final_score(self, ca_score, exam_score):
        return ca_score + exam_score

    def calculate_grade(self, final_score):
        if final_score >= 70:
            return "A", 4.0
        elif final_score >= 60:
            return "B+", 3.5
        elif final_score >= 50:
            return "B", 3.0
        elif final_score >= 45:
            return "C+", 2.5
        else:
            return "F", 0.0

    def update_course_display(self, *args):
        course = self.selected_course.get()
        course_info = self.course_data[course]

        # Update Lecturer and Course Code
        self.lecturer_label.configure(text=f"Lecturer: {course_info['lecturer']}")
        self.code_label.configure(text=f"Course Code: {course_info['code']}")

        # Update Table that is deletes the existing rows
        for row in self.tree.get_children():# collects all the subattributes of our table
            self.tree.delete(row)

        for student in course_info["students"]:
            final_score = self.calculate_final_score(student["caScore"], student["examScore"])
            grade, credit = self.calculate_grade(final_score)
            self.tree.insert("", "end", values=(
                student["name"],
                student["mat"],
                student["caScore"],
                student["examScore"],
                final_score,
                grade,
                f"{credit:.1f}"
            ))

    def open_add_student_form(self):
        form_window = ctk.CTkToplevel(self)
        form_window.title("Add Student")
        form_window.geometry("400x500")
        form_window.configure(fg_color=BACKGROUND_COLOR)

        ctk.CTkLabel(form_window, text="Add Student", font=("Arial", 24, "bold"), text_color=PRIMARY_COLOR).pack(
            pady=20)

        fields = [
            ("Name", "name"),
            ("Matriculation Number", "mat"),
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
        course_var = ctk.StringVar(value=list(self.course_data.keys())[0])
        course_menu = ctk.CTkOptionMenu(course_frame, variable=course_var, values=list(self.course_data.keys()),
                                        fg_color=PRIMARY_COLOR, button_color=PRIMARY_COLOR,
                                        button_hover_color=ACCENT_COLOR,
                                        dropdown_fg_color=BACKGROUND_COLOR, dropdown_hover_color=SECONDARY_COLOR,
                                        dropdown_text_color=TEXT_COLOR)
        course_menu.pack(side="right", padx=10, pady=5, fill="x", expand=True)

        def submit():
            course = course_var.get()
            try:
                new_student = {
                    "name": entries["name"].get(),
                    "mat": entries["mat"].get(),
                    "caScore": int(entries["ca"].get()),
                    "examScore": int(entries["exam"].get()),
                }
                self.course_data[course]["students"].append(new_student)
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


if __name__ == "__main__":
    app = AdminDashboardApp()
    app.mainloop()

