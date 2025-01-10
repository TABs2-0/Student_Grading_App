import customtkinter as ctk  # type: ignore
from PIL import Image, ImageTk  # type: ignore
# from student_grading_app import view # type:ignore
from customtkinter import CTkImage  # type: ignore


def forgot_password_action():
    # Action pour le bouton "Mot de passe oublié ?"
    print(
        "L'option 'Mot de passe oublié ?' a été sélectionnée. Veuillez suivre la procédure de récupération du mot de passe.")


class MyAccountApp(ctk.CTk):
    def __init__(self):
        super().__init__()  # Définir la couleur de fond de la fenêtre principale

        # Créer la fenêtre principale

        self.title("MyAccountApp")
        self.geometry("500x500")  # Corrected geometry method call

        # Créer un frame pour les widgets avec un fond orange
        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True)  # Adjust frame to fill the entire window

        # Créer un label
        label = ctk.CTkLabel(frame, text="My Account", font=("Arial", 24, "bold"), width=200, height=35,
                             corner_radius=20, fg_color="white", bg_color="purple")
        label.grid(column=3)

        # Use CTkImage for better scaling on  displays
        user_image = Image.open(
            r"C:\Users\Tab's\PycharmProjects\SGApp\IMG\my account.jpg")
        self.image = CTkImage(user_image, size=(100, 100))
        self.image_label = ctk.CTkLabel(frame, text=' ', image=self.image, bg_color="purple",
                                        corner_radius=15)  # ,bg_color="purple")
        self.image_label.grid(pady=10, column=0, row=0)
        school_image = Image.open(
            r"C:\Users\Tab's\PycharmProjects\SGApp\IMG\school.jpg")

        self.image = CTkImage(school_image, size=(100, 100))
        self.image_label = ctk.CTkLabel(frame, text=" ", image=self.image)
        self.image_label.grid(column=3, row=16, pady=40)

        # Création des labels et des champs de saisie avec des valeurs par défaut
        self.label_username = ctk.CTkLabel(frame, text="Username  :")
        self.label_username.grid(row=3, column=1, pady=10, )
        self.label_matricule = ctk.CTkLabel(frame, text="User123", width=200, height=25, corner_radius=10,
                                            fg_color="white", bg_color="purple")
        # self.label_matricule.insert(0, "ICTU20234009")
        self.label_matricule.grid(row=3, column=3)

        self.label_email = ctk.CTkLabel(frame, text="Email  :")
        self.label_email.grid(row=5, column=1)
        self.label_email = ctk.CTkLabel(frame, width=200, text='Admin@gmail.coom', height=25, corner_radius=15,
                                        fg_color="white", bg_color="purple")

        self.label_email.grid(row=5, column=3, padx=10)

        # Ajout du champ Mot de passe
        self.label_Role = ctk.CTkLabel(frame, text=" Role  :")
        self.label_Role.grid(row=7, column=1, pady=10)
        self.label_Role = ctk.CTkLabel(frame, text="Student/Admin/Lecturer", width=200, height=25, corner_radius=10,
                                       fg_color="white", bg_color="purple")

        self.label_Role.grid(row=7, column=3, padx=10, pady=10)

        # CheckBox pour afficher/masquer le mot de passe
        '''self.show_password_var = ctk.BooleanVar()
        self.checkbox_show_password = ctk.CTkCheckBox(frame, text="Show/Hide", variable=self.show_password_var, command=self.toggle_password_visibility)
        self.checkbox_show_password.grid(pady=10 ,row=7, column=4 ,padx=5)'''

        # Bouton pour "Mot de passe oublié ?"
        '''self.button_forgot_password = ctk.CTkButton(frame, text="Forgotten Password?",
                                                    command=forgot_password_action)
        self.button_forgot_password.grid(row=10,column=3, pady=15,padx=5 )'''

        # Création d'un bouton pour se déconnecter
        self.button_logout = ctk.CTkButton(frame, text="Log Out", fg_color="purple", command=self.logout_action)
        self.button_logout.grid(column=3, row=12, pady=30)

    def toggle_password_visibility(self):
        # Basculer la visibilité du mot de passe
        if self.show_password_var.get():
            self.label_password.configure(show="")  # Show password
        else:
            self.label_password.configure(show="*")  # Hide password

    def logout_action(self):
        # Action lorsque le bouton "Log Out" est cliqué
        print("Déconnexion de l'utilisateur")
        self.quit()  # Ferme l'application


#if __name__ == "__main__":
 #   app = MyAccountApp()
  #  app.mainloop()
