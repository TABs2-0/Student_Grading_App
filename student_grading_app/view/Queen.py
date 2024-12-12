from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk  # Import PIL modules
import tkinter as tk

class MyFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Add widgets onto the frame
        self.label = CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title('Admin Page')
        self.geometry("600x600")
        # Set up canvas for background image

        # Load the image (replace with your image file path)
        self.bg_image = Image.open("C:/Users/Tab's/PycharmProjects/SGApp/IMG/Button_Background-Images.jpg")
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)

        self.canvas = CTkCanvas(self,height=600,width=600)
        self.canvas.pack(fill="both", expand=True)
        self.bg_image_on_canvas = self.canvas.create_image(370, 370, image=self.bg_image_tk, anchor="center")


        # Display the background imagee

        # Creating combobox on the canvas
        self.combo_box = CTkComboBox(self, values=["Prob and Stat", "Comp Org", "Python", "Java"],
                                     command=self.change_mode)
        self.combo_box_window = self.canvas.create_window(300, 50, window=self.combo_box)

        # Frame for the table on the canvas
        self.table_frame = CTkFrame(self)
        self.table_frame_window = self.canvas.create_window(350, 350, window=self.table_frame)

        # Bind window resizing to the update_background method
        self.bind("<Configure>", self.update_background)

    def update_background(self, event):
        # Resize the background image based on the current window size
        width, height = event.width, event.height
        resized_bg = self.bg_image.resize((width, height))
        self.bg_image_tk = ImageTk.PhotoImage(resized_bg)

        # Update the background image on the canvas
        self.canvas.itemconfig(self.bg_image_on_canvas, image=self.bg_image_tk)

    def change_mode(self, choice):
        # Clear previous table data
        self.clear_table()

        # Fetch and display data for the selected subject
        if choice in student_data:
            data = student_data[choice]
            self.populate_table(data)

    def clear_table(self):
        # Remove all widgets from the table frame
        for widget in self.table_frame.winfo_children():
            widget.destroy()

    def populate_table(self, data):
        # Create table headers
        for col_index, header in enumerate(data[0]):
            header_label = CTkLabel(self.table_frame, text=header)
            header_label.grid(row=0, column=col_index, padx=5, pady=5)

        # Create table rows
        for row_index, row in enumerate(data[1:], start=1):
            for col_index, value in enumerate(row):
                value_label = CTkLabel(self.table_frame, text=value)
                value_label.grid(row=row_index, column=col_index, padx=10, pady=10)


# Student data
student_data = {
    "Prob and Stat": [["name", "mat", "ca", "exam", "final"],
                      ["John ode", "ICTU2021333E", 30, 50, 80],
                      ["no 2", "ICTU2021333E", 30, 10, 40],
                      ["no4", "ICTU2021333E", 30, 70, 100]],
    "Comp Org": [["name", "mat", "ca", "exam", "final"],
                 ["Mayt", "ICTU2021333E", 30, 50, 80],
                 ["Sam 2", "ICTU2021333E", 30, 10, 40],
                 ["JOHNY", "ICTU2021333E", 30, 70, 100]],
    "Python": [["name", "mat", "ca", "exam", "final"],
               ["nathan", "ICTU2021333E", 30, 50, 80],
               ["Joe", "ICTU2021333E", 30, 10, 40],
               ["swaw", "ICTU2021333E", 30, 70, 100]],
    "Java": [["name", "mat", "ca", "exam", "final"],
             ["remw", "ICTU2021333E", 30, 50, 80],
             ["no 10", "ICTU2021333E", 30, 10, 40],
             ["no3", "ICTU2021333E", 30, 70, 100]],
}

# Create and run the application
app = App()
app.mainloop()
