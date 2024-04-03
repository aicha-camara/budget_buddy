import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import ttk
from database import create_user
from validator import Validator
from database import show_transactions
from database import get_solde
import matplotlib.pyplot as plt

class Frames:
    def __init__(self, root):
        self.info_frame = None
        self.main_container = None
        self.root = root
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
        ttk.Label(login_frame, text="Nom").pack()
        lastname_entry = ttk.Entry(login_frame)
        lastname_entry.pack()

        # Add a label and entry for the username
        ttk.Label(login_frame, text="Prenom").pack()
        name_entry = ttk.Entry(login_frame)
        name_entry.pack()

        # Add a label and entry for the password
        ttk.Label(login_frame, text="Mot de passe").pack()
        password_entry = ttk.Entry(login_frame, show="*")
        password_entry.pack()

        # Add a login button that calls the login method with the entered username and password
        ttk.Button(login_frame, text="Connexion",
                   command=lambda: self.login(lastname_entry, name_entry, password_entry)).pack(pady=10)

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
                   command=lambda: self.register(lastname_entry.get(), name_entry.get(),
                                                 email_entry.get(), password_entry.get(),
                                                 confirm_password_entry.get())).pack(pady=10)

        # Add a back button that shows the welcome frame
        ttk.Button(registration_frame, text="Retour",
                   command=lambda: self.show_frame(self.welcome_frame)).pack(pady=10)

        # Return the completed registration frame
        return registration_frame

    # Validate registration and create user if valid

    def login(self, lastname_entry, name_entry, password_entry):
        # Get the entered username and password
        lastname_entre = lastname_entry.get()
        name_entre = name_entry.get()
        mot_de_passe_entre = password_entry.get()

        # Validate the login details
        if not Validator.validate_login(lastname_entre, name_entre, mot_de_passe_entre):
            # Show error message if validation fails

            return
        pseudo = (lastname_entre, name_entre)
        transactions = show_transactions(lastname_entre, name_entre)
        # If validation is successful, proceed to main frame creation
        self.root.withdraw()
        self.create_main_frame(pseudo, transactions)

    def register(self, lastname, name, email, password, confirm_password):
        # Validate the registration details
        if not Validator.validate_registration(lastname, name, email, password, confirm_password):
            return

        # If validation is successful, create a new user
        create_user(lastname, name, email, password)

        # Show a success message to the user
        msgbox.showinfo("Succès", "Inscription réussie. Vous pouvez maintenant vous connecter.")

        # Show the login frame
        self.show_frame(self.login_frame)

    @staticmethod
    def show_transactions_table(info_frame, headers, transactions):
        # Display transactions in a table format
        for idx, transaction in enumerate(transactions):
            for col, value in enumerate(transaction):
                label = ttk.Label(info_frame, text=value, font=("Verdana", 10), background="#36393e",
                                  foreground="white")

                # Change color based on sign of the amount
                if col == 2:  # Assuming montant is at index 2 in the transactions list
                    montant = float(value)
                    if montant > 0:
                        label.config(foreground="green")
                    elif montant < 0:
                        label.config(foreground="red")

                label.grid(row=idx + 2, column=col, sticky="ew", padx=5, pady=5)

        # Add separator after transactions
        ttk.Separator(info_frame, orient="horizontal").grid(row=len(transactions) + 2, columnspan=len(headers),
                                                            sticky="ew", pady=5)

    def disconnect(self):
        # Fermer la fenêtre principale
        self.main_frame.destroy()

    def create_main_frame(self, pseudo, transactions):
        lastname, name = pseudo

        # Create a new top-level window for the main frame
        self.main_frame = tk.Toplevel(self.root)
        self.main_frame.title("Bank")

        # Set background color of the main frame
        self.main_frame.configure(bg="#282b30")

        # Load the background image
        self.background_image = tk.PhotoImage(file="assets/pattern.png")
        # Create a label to hold the background image
        background_label = ttk.Label(self.main_frame, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a new frame to hold all the elements
        main_container = tk.Frame(self.main_frame, background="#282b30")
        main_container.pack(fill="both", expand=True, padx=20, pady=20)  # Added padding

        # Add a label to display the username
        ttk.Label(main_container, text="Re-bonjour " + lastname + " " + name + " !", font=("Verdana", 15),
                  background="#282b30", foreground="white").pack(
            side=tk.TOP, pady=10)

        # Créer un label pour afficher le solde avec récupération directe depuis la base de données
        ttk.Label(main_container, text="Solde: " + str(get_solde(lastname, name)), font=("Verdana", 12),
                  background="#282b30", foreground="white").pack(
            side=tk.TOP, pady=10)

        ttk.Label(main_container, text="Connecté en tant que: " + lastname + " " + name, background="#282b30",
                  foreground="white").pack(side=tk.BOTTOM, pady=10)
        ttk.Button(main_container, text="Déconnexion", command=self.disconnect).pack(side=tk.BOTTOM, pady=10)

        # Create a new frame to display additional information
        info_frame = tk.Frame(main_container, background="#36393e")
        info_frame.pack(side=tk.TOP, padx=10, pady=10, fill="both", expand=True)  # Added fill and expand

        # Headers for the columns
        headers = ["Nom", "Description", "Montant", "Type", "Date"]

        def sort_transactions(col_index):
            if col_index != 1:  # Do not sort if the column index corresponds to the Description column
                # Clear existing transaction rows in the info_frame
                for widget in info_frame.winfo_children():
                    if isinstance(widget, ttk.Label):
                        widget.destroy()

                sorted_transactions = sorted(transactions, key=lambda x: x[col_index])
                self.show_transactions_table(info_frame, headers, sorted_transactions)

        # Create clickable headers
        for col, header in enumerate(headers):
            ttk.Button(info_frame, text=header, command=lambda col_index=col: sort_transactions(col_index)).grid(
                row=0, column=col, padx=5, pady=5, sticky="ew")  # Added sticky

        # Show initial transactions table
        # Show initial transactions table
        self.show_transactions_table(info_frame, headers, transactions)

        # Create and display expenses by month graph
        self.create_graph(transactions)

    @staticmethod
    def create_graph(transactions):
        # Créer un dictionnaire pour stocker les dépenses par mois
        expenses_by_month = {}

        # Parcourir toutes les transactions et calculer les dépenses par mois
        for transaction in transactions:
            # Convertir la date en format "AAAA-MM-JJ" en chaîne de caractères
            date_str = transaction[4].strftime("%Y-%m-%d")
            month = date_str.split("-")[1]  # Extraire le mois
            montant = float(transaction[2])  # La colonne 2 contient le montant de la transaction

            # Vérifier si la transaction est une dépense (montant négatif)
            if montant < 0:
                if month not in expenses_by_month:
                    expenses_by_month[month] = 0
                expenses_by_month[month] += abs(montant)  # Ajouter la valeur absolue du montant à la dépense mensuelle

        # Trier les mois par ordre croissant
        sorted_months = sorted(expenses_by_month.keys())

        # Extraire les dépenses et les mois triés
        expenses = [expenses_by_month[month] for month in sorted_months]
        months = [f'Mois {month}' for month in
                  sorted_months]  # Vous pouvez utiliser le nom complet du mois si disponible

        # Créer le graphique
        plt.figure(figsize=(10, 6))
        plt.plot(months, expenses, marker='o', linestyle='-')
        plt.xlabel('Mois')
        plt.ylabel('Dépenses (€)')
        plt.title('Dépenses par mois')
        plt.xticks(rotation=45)  # Faire pivoter les étiquettes des mois pour une meilleure lisibilité
        plt.tight_layout()
        plt.savefig('expenses_by_month_graph.png')
        # Afficher le graphique
        plt.show()
