import tkinter as tk
from tkinter import ttk


def go_to_account():
    print("Account Page")

def list_levels():
    levels_dropdown["state"] = "readonly"

def list_semesters():
    semester_dropdown["state"] = "readonly"

def view_grades():
    selected_level = levels_var.get()
    selected_semester = semester_var.get()
    if selected_level and selected_semester:
        print(f"Choix : Niveau - {selected_level}, Semestre - {selected_semester}")
    else:
        print("Veuillez sélectionner un niveau et un semestre.")

root = tk.Tk()
root.title("Student Interface")
root.geometry("600x400")
root.configure(bg="#FFFFFF")  


account_button = tk.Button(root, text="Account", command=go_to_account, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
account_button.place(x=20, y=20, width=100, height=40)


title_label = tk.Label(root, text="Student Portal", font=("Arial", 18, "bold"), bg="#FFFFFF", fg="#333333")
title_label.place(x=200, y=20)

level_button = tk.Button(root, text="Level", command=list_levels, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
level_button.place(x=50, y=100, width=100, height=40)

levels_var = tk.StringVar()
levels_dropdown = ttk.Combobox(root, textvariable=levels_var, values=["Level 1", "Level 2", "Level 3", "Level 4"], state="disabled", font=("Arial", 12))
levels_dropdown.place(x=200, y=100, width=200, height=40)

semester_button = tk.Button(root, text="Semester", command=list_semesters, bg="#FF9800", fg="white", font=("Arial", 12, "bold"))
semester_button.place(x=50, y=180, width=100, height=40)

semester_var = tk.StringVar()
semester_dropdown = ttk.Combobox(root, textvariable=semester_var, values=["Fall", "Spring", "Summer"], state="disabled", font=("Arial", 12))
semester_dropdown.place(x=200, y=180, width=200, height=40)

view_button = tk.Button(root, text="View", command=view_grades, bg="#F44336", fg="white", font=("Arial", 14, "bold"))
view_button.place(x=250, y=280, width=100, height=50)

root.mainloop()