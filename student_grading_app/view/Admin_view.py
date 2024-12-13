import customtkinter
from tkinter import Canvas
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from customtkinter import CTkLabel, CTkComboBox, CTkCanvas, CTkFrame, CTk


#QEEN's WORK, Still have to connect our two ui's

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
        self.image_reference = self.bg_image_tk

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
        self._image = Image.open("C:/Users/Tab's/PycharmProjects/SGApp/IMG/pexels-karolina-grabowska-5477714.jpg").resize(
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

        self.Logout_IMG_2 = ctk.CTkImage(Image.open("C:/Users/Tab's/PycharmProjects/SGApp/IMG/5528144.png"))
        self.button_background_image = ctk.CTkImage(
            Image.open("C:/Users/Tab's/PycharmProjects/SGApp/IMG/Button_Background-Images.jpg"))
        self.log_out__button = ctk.CTkButton(master=self.Nav_1, image=self.Logout_IMG_2, corner_radius=5,
                                             text="Log_Out")
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
                                     font=("Roboto", 15), image=self.button_background_image, command=self.display)
                List.grid(row=0, column=semesters.index(semester), pady=5, padx=5)

    # the function below is the to apply the animation
    def animate_text(self, index):
        max_index= len(self.text)-1
        if index < len(self.text):
            self.Nav.configure(text=self.Nav.cget("text") + self.text[self.current_index])
            self.current_index +=1
            self.after(250, self.animate_text, index + 1)
        else:
            pass
    # the function below will be modified to consider the level and semesters from the db
    def display(self):
        self.withdraw()

        app = App()
        app.mainloop()
A=Adminhome()
A.mainloop()