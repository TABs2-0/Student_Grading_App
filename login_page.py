import customtkinter as ctk


# ctk.set_appearance_mode("dark")


def forgot_password_action():
    # Action pour le bouton "Mot de passe oublié ?"
    print(
        "L'option 'Mot de passe oublié ?' a été sélectionnée. Veuillez suivre la procédure de récupération du mot de passe.")


class MyAccountApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Définir la couleur de fond de la fenêtre principale
        self.configure(bg="#87CEEB")  # Bleu ciel

        # Créer la fenêtre principale
        self.title("MyAccountApp")
        self.geometry("600*600")

        # Créer un frame pour les widgets avec un fond orange
        frame = ctk.CTkFrame(self, )
        frame.grid(ipadx=10)

        # Créer un label
        label = ctk.CTkLabel(frame, text="My Account", font=("Arial", 24, "bold"))
        label.grid(column=3)

        # Création des labels et des champs de saisie avec des valeurs par défaut
        self.label_username = ctk.CTkLabel(frame, text="ID  :")
        self.label_username.grid(row=3, column=1, pady=10)
        self.entry_matricule = ctk.CTkEntry(frame, bg_color="white")
        self.entry_matricule.insert(0, "ICTU20234009")  # Valeur par défaut
        self.entry_matricule.grid(row=3, column=3)

        self.label_email = ctk.CTkLabel(frame, text="Email  :")
        self.label_email.grid(row=5, column=1)
        self.entry_email = ctk.CTkEntry(frame, bg_color="white")
        self.entry_email.insert(0, "daryl.tiessi@gmail.com")  # Valeur par défaut
        self.entry_email.grid(row=5, column=3, padx=10)

        # Ajout du champ Mot de passe
        self.label_password = ctk.CTkLabel(frame, text=" Password  :")
        self.label_password.grid(row=7, column=1, pady=10)
        self.entry_password = ctk.CTkEntry(frame, bg_color="white", show="*")
        self.entry_password.insert(0, "password")  # Valeur par défaut
        self.entry_password.grid(row=7, column=3, padx=10, pady=10)

        # CheckBox pour afficher/masquer le mot de passe
        self.show_password_var = ctk.BooleanVar()
        self.checkbox_show_password = ctk.CTkCheckBox(frame, text="Show/Hide", variable=self.show_password_var,
                                                      command=self.toggle_password_visibility)
        self.checkbox_show_password.grid(pady=10, row=7, column=4, padx=5)

        # Bouton pour "Mot de passe oublié ?"
        self.button_forgot_password = ctk.CTkButton(frame, text="Forgotten Password?",
                                                    command=forgot_password_action)
        self.button_forgot_password.grid(column=3, pady=15, padx=5)

        # Création d'un bouton pour se déconnecter
        self.button_logout = ctk.CTkButton(frame, text="Log Out", fg_color="red", command=self.logout_action)
        self.button_logout.grid(column=3)

    def toggle_password_visibility(self):
        # Basculer la visibilité du mot de passe
        if self.show_password_var.get():
            self.entry_password.configure(show="")
        else:
            self.entry_password.configure(show="*")

    def logout_action(self):
        # Action lorsque le bouton "Log Out" est cliqué
        username = self.entry_username.get()
        matricule = self.entry_matricule.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        print("Déconnexion de l'utilisateur :", username)
        print("Matricule :", matricule)
        print("Email :", email)
        print("Mot de passe :", password)
        self.quit()  # Ferme l'application


if __name__ == "__main__":
    app = MyAccountApp()
    app.mainloop()
