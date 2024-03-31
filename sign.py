import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import ttk
from database import create_user
from validator import Validator

class Frames:
    def __init__(self, root):
        self.root = root
        self.username = None
        self.main_frame = None
        self.message_area = None
        self.message_container = None
        self.message_entry = None
        self.send_button = None
        self.background_image = None

        # Create initial frames
        self.login_frame = self.create_login_frame()
        self.registration_frame = self.create_registration_frame()
        self.welcome_frame = self.create_welcome_frame()

    # Hide all frames and show the specified one
    def show_frame(self, frame):
        for f in (self.welcome_frame, self.login_frame, self.registration_frame):
            f.pack_forget()
        frame.pack(fill="both", expand=True)

    # Create and return the welcome frame
    def create_welcome_frame(self):
        # Create a new frame for the welcome screen
        welcome_frame = ttk.Frame(self.root)

        # Load the background image
        self.background_image = tk.PhotoImage(file="assets/pattern.png")
        # Create a label to hold the background image
        background_label = ttk.Label(welcome_frame, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a container for all elements
        container = ttk.Frame(welcome_frame)
        container.pack(expand=True)

        # Add a welcome label to the container
        ttk.Label(container, text="Bonjour cher client!", font=("Helvetica", 16)).pack(pady=20)

        # Create a container for the buttons
        button_container = ttk.Frame(container)
        button_container.pack(pady=10)

        # Add a login button to the button container
        ttk.Button(button_container, text="Se connecter",
                   command=lambda: self.show_frame(self.login_frame)).pack(side=tk.LEFT, padx=10)

        # Add a registration button to the button container
        ttk.Button(button_container, text="S'inscrire",
                   command=lambda: self.show_frame(self.registration_frame)).pack(side=tk.LEFT, padx=10)

        # Return the completed welcome frame
        return welcome_frame

    # Create and return the login frame
    def create_login_frame(self):
        # Create a new frame for the login screen
        login_frame = ttk.Frame(self.root)

        # Add a title label to the frame
        ttk.Label(login_frame, text="Connexion", font=("Arial", 16)).pack(pady=10)

        # Add a label and entry for the username
        ttk.Label(login_frame, text="Email/Nom d'utilisateur").pack()
        username_entry = ttk.Entry(login_frame)
        username_entry.pack()

        # Add a label and entry for the password
        ttk.Label(login_frame, text="Mot de passe").pack()
        password_entry = ttk.Entry(login_frame, show="*")
        password_entry.pack()

        # Add a login button that calls the login method with the entered username and password
        ttk.Button(login_frame, text="Connexion",
                   command=lambda: self.login(username_entry, password_entry)).pack(pady=10)

        # Add a back button that shows the welcome frame
        ttk.Button(login_frame, text="Retour",
                   command=lambda: self.show_frame(self.welcome_frame)).pack(pady=10)

        # Return the completed login frame
        return login_frame

    # Create and return the registration frame
    def create_registration_frame(self):
        # Create a new frame for the registration screen
        registration_frame = ttk.Frame(self.root)

        # Add a title label to the frame
        ttk.Label(registration_frame, text="Inscription", font=("Arial", 16)).pack(pady=10)

        # Add a label and entry for the lastname
        ttk.Label(registration_frame, text="Nom").pack()
        lastname_entry = ttk.Entry(registration_frame)
        lastname_entry.pack()

        # Add a label and entry for the name
        ttk.Label(registration_frame, text="Prénom").pack()
        name_entry = ttk.Entry(registration_frame)
        name_entry.pack()

        # Add a label and entry for the username
        ttk.Label(registration_frame, text="Nom d'utilisateur").pack()
        username_entry = ttk.Entry(registration_frame)
        username_entry.pack()

        # Add a label and entry for the email
        ttk.Label(registration_frame, text="Email").pack()
        email_entry = ttk.Entry(registration_frame)
        email_entry.pack()

        # Add a label and entry for the password
        ttk.Label(registration_frame, text="Mot de passe").pack()
        password_entry = ttk.Entry(registration_frame, show="*")
        password_entry.pack()

        # Add a label and entry for the password confirmation
        ttk.Label(registration_frame, text="Confirmer le mot de passe").pack()
        confirm_password_entry = ttk.Entry(registration_frame, show="*")
        confirm_password_entry.pack()

        # Add a registration button that calls the register method with the entered details
        ttk.Button(registration_frame, text="Inscription",
                   command=lambda: self.register(lastname_entry.get(), name_entry.get(), username_entry.get(),
                                                 email_entry.get(), password_entry.get(),
                                                 confirm_password_entry.get())).pack(pady=10)

        # Add a back button that shows the welcome frame
        ttk.Button(registration_frame, text="Retour",
                   command=lambda: self.show_frame(self.welcome_frame)).pack(pady=10)

        # Return the completed registration frame
        return registration_frame

    # Validate registration and create user if valid

    def login(self, username_entry, password_entry):
        # Get the entered username and password
        pseudo_entre = username_entry.get()
        mot_de_passe_entre = password_entry.get()

        # Validate the login details
        if not Validator.validate_login(pseudo_entre, mot_de_passe_entre):
            # Show error message if validation fails

            return

        # If validation is successful, proceed to main frame creation
        self.root.withdraw()
        self.create_main_frame(pseudo_entre)

    def register(self, lastname, name, username, email, password, confirm_password):
        # Validate the registration details
        if not Validator.validate_registration(username, email, password, confirm_password):
            return

        # If validation is successful, create a new user
        create_user(lastname, name, username, email, password)

        # Show a success message to the user
        msgbox.showinfo("Succès", "Inscription réussie. Vous pouvez maintenant vous connecter.")

        # Show the login frame
        self.show_frame(self.login_frame)

    def create_main_frame(self, username):
        # Create a new top-level window for the main frame
        self.main_frame = tk.Toplevel(self.root)
        self.main_frame.title("MyDiscord")

        # Add a label to display the username
        ttk.Label(self.main_frame, text="Connecter en tant que: " + username).pack(side=tk.TOP)
