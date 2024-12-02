import customtkinter
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk


#QEEN's WORK, Still have to connect our two ui's

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Add widgets onto the frame
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)



class App(customtkinter.CTk):
    # Defaulting to light mode
    customtkinter.set_appearance_mode("dark")

    def __init__(self):
        super().__init__()
        self.title('Admin Page')
        self.geometry("700x700")
        self.resizable(False,False)

        # Creating combobox
        self.combo_box = customtkinter.CTkComboBox(self, values=["Prob and Stat", "Comp Org", "Python", "Java"],
                                                   command=self.change_mode)
        self.combo_box.pack(padx=20, pady=20)

        # Label to display the selected data
        self.data_display = customtkinter.CTkLabel(self, text="")
        self.data_display.pack(padx=20, pady=20)

    def change_mode(self, choice):
        # Change appearance mode (this is just an example; you might want to handle it differently)
        customtkinter.set_appearance_mode(choice)

        # Fetch and display data for the selected subject
        if choice in student_data:
            data = student_data[choice]
            formatted_data = "\n".join([", ".join(map(str, row)) for row in data])
            self.data_display.configure(text=formatted_data)
        else:
            self.data_display.configure(text="")


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

MyFrame.bind


#MY WORK
def display_semester_buttons():
    semesters = ["Fall", "Spring", "Summer"]

    display = customtkinter.CTk()
    frame_2 = customtkinter.CTkFrame(master=display, width=200, height=700, fg_color="#FF7F50")  # orange Frame
    frame_2.pack(pady=50, padx=10, expand=True, anchor="se", side="right")
    for semester in semesters:
        List = customtkinter.CTkButton(master=frame_2, fg_color="#000080", text=semester, font=("Roboto", 15))
        List.pack(side="left", padx=5)
    display.mainloop()


class Adminhome(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        Levels = ["Level One", "Level Two", "Level Three", "Level Four"]
        customtkinter.set_appearance_mode("dark")
        self.title("Admin_Page")
        self.geometry("750x750")
        semesters = ["Fall", "Spring", "Summer"]
        self.resizable(False, False)

        #background_Image

        self.background_image = Image.open("C:/Users/Tab's/PycharmProjects/SGApp/IMG/Old-School-Image (1).png").resize(
            (750, 750))
        self.background_photo = ImageTk.PhotoImage(self.background_image, size=(10, 30))

        # Create a canvas to hold the background image
        self.canvas = tk.Canvas(self, width=750, height=750)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="center")

        #Nav for other widgets like myaccount
        # the image has not yet been inserted
        self.Nav_1 = ctk.CTkLabel(master=self.canvas, width=10, height=20, text="")
        self.Nav_1.pack()
        self.MyAccount_IMG_1 = customtkinter.CTkImage(
            light_image=Image.open("C:/Users/Tab's/PycharmProjects/SGApp/IMG/myaccount.png"), size=(30, 30))

        self.account_button = customtkinter.CTkButton(master=self.Nav_1, image=self.MyAccount_IMG_1, text="My Account",
                                                      corner_radius=5)

        self.account_button.grid(row=0, column=0, padx=10, sticky="w")
        self.Logout_IMG_2 = customtkinter.CTkImage(Image.open("C:/Users/Tab's/PycharmProjects/SGApp/IMG/5528144.png"))
        self.button_background_image = customtkinter.CTkImage(
            Image.open("C:/Users/Tab's/PycharmProjects/SGApp/IMG/Button_Background-Images.jpg"))
        self.log_out__button = customtkinter.CTkButton(master=self.Nav_1, image=self.Logout_IMG_2, corner_radius=5,
                                                       text="Log_Out")
        self.log_out__button.grid(padx=300, pady=0, sticky="e", ipadx=500)

        self.text = " 𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕋𝕠 𝕐𝕠𝕦𝕣 ℍ𝕠𝕞𝕖 ℙ𝕒𝕘𝕖 𝔸𝕕𝕞𝕚𝕟 𝕁𝕖𝕗𝕗"  #home page text
        self.Nav = ctk.CTkLabel(master=self, width=10, height=20, anchor="center",
                                font=("Retro cool", 24), text=self.text, text_color="white")
        self.Nav.pack()
        self.animate_text(0)

        #frame for the semester butons display
        self.frame_0 = ctk.CTkFrame(master=self, width=200, height=700,
                                    fg_color="#000080")  # Blue
        self.frame_0.pack(pady=50, padx=10, anchor="w", side="right")

        #  frame for the level display
        self.frame = ctk.CTkFrame(master=self, width=300, height=700, fg_color="#000080")  # Blue
        self.frame.pack(pady=50, padx=10, anchor="sw", side="left")

        # semester buttons for each semester
        self.frame_1 = ctk.CTkFrame(master=self.frame, width=200, height=700, fg_color="#000080")
        self.frame_1.pack(fill="y", expand=True)

        for j in range(4):
            self.level = customtkinter.CTkLabel(master=self.frame_1, fg_color="grey", text=Levels[j],
                                                font=("Arial", 12))
            self.level.pack(pady=75, anchor="center")
        for i in range(0, 4):
            self.frame_2 = ctk.CTkFrame(master=self.frame_0, width=200, height=700, fg_color="#FF7F50")  # orange Frame
            self.frame_2.pack(pady=20, padx=10, expand=True,
                              side="top")  # Adjusting padding and side to display our respective semesters

            for semester in semesters:
                List = ctk.CTkButton(master=self.frame_2, width=100, height=100, fg_color="#000080", text=semester,
                                     font=("Roboto", 15), image=self.button_background_image, command=self.display)
                List.pack(side="left", pady=5)

    # the function below is the to apply the animation
    def animate_text(self, index):
        if index <= len(self.text):
            self.Nav.configure(text=self.Nav.cget("text") + self.text[index])
            self.after(250, self.animate_text, index + 1)

# the function below will be modified to consider the level and semesters from the db
    def display(self):
        self.withdraw()

        app = App()
        app.mainloop()


admin_home = Adminhome()
admin_home.mainloop()
