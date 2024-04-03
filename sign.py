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

        # Créer les frames initiales
        self.login_frame = self.create_login_frame()
        self.registration_frame = self.create_registration_frame()
        self.welcome_frame = self.create_welcome_frame()

    # Masquer toutes les frames et afficher celle spécifiée
    def show_frame(self, frame):
        for f in (self.welcome_frame, self.login_frame, self.registration_frame):
            f.pack_forget()
        frame.pack(fill="both", expand=True)

    # Créer et retourner la frame de bienvenue
    def create_welcome_frame(self):
        # Créer une nouvelle frame pour l'écran de bienvenue
        welcome_frame = ttk.Frame(self.root)

        # Charger l'image de fond
        self.background_image = tk.PhotoImage(file="assets/pattern.png")
        # Créer une étiquette pour contenir l'image de fond
        background_label = ttk.Label(welcome_frame, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Créer un conteneur pour tous les éléments
        container = tk.Frame(welcome_frame, background="#282b30")
        container.pack(expand=True)

        # Ajouter une étiquette de bienvenue au conteneur
        ttk.Label(container, text="Bienvenue sur mybudget!", background="#282b30", foreground="white",
                  font=("Helvetica", 16)).pack(pady=20)

        # Créer un conteneur pour les boutons
        button_container = tk.Frame(container, background="#282b30")
        button_container.pack(pady=10)

        # Ajouter un bouton de connexion au conteneur de boutons
        ttk.Button(button_container, text="Se connecter",
                   command=lambda: self.show_frame(self.login_frame)).pack(side=tk.LEFT, padx=10)

        # Ajouter un bouton d'inscription au conteneur de boutons
        ttk.Button(button_container, text="S'inscrire",
                   command=lambda: self.show_frame(self.registration_frame)).pack(side=tk.LEFT, padx=10)

        # Retourner la frame de bienvenue complétée
        return welcome_frame

    # Créer et retourner la frame de connexion
    def create_login_frame(self):
        # Créer une nouvelle frame pour l'écran de connexion
        login_frame = ttk.Frame(self.root)
        # Ajouter une étiquette de titre à la frame
        ttk.Label(login_frame, text="Connexion", font=("Arial", 16)).pack(pady=10)

        # Ajouter une étiquette et une entrée pour le nom
        ttk.Label(login_frame, text="Nom").pack()
        lastname_entry = ttk.Entry(login_frame)
        lastname_entry.pack()

        # Ajouter une étiquette et une entrée pour le prénom
        ttk.Label(login_frame, text="Prénom").pack()
        name_entry = ttk.Entry(login_frame)
        name_entry.pack()

        # Ajouter une étiquette et une entrée pour le mot de passe
        ttk.Label(login_frame, text="Mot de passe").pack()
        password_entry = ttk.Entry(login_frame, show="*")
        password_entry.pack()

        # Ajouter un bouton de connexion qui appelle la méthode de connexion
        # avec le nom d'utilisateur et le mot de passe saisis
        ttk.Button(login_frame, text="Connexion",
                   command=lambda: self.login(lastname_entry, name_entry, password_entry)).pack(pady=10)

        # Ajouter un bouton de retour qui affiche la frame de bienvenue
        ttk.Button(login_frame, text="Retour",
                   command=lambda: self.show_frame(self.welcome_frame)).pack(pady=10)

        # Retourner la frame de connexion complétée
        return login_frame

    # Créer et retourner la frame d'inscription
    def create_registration_frame(self):
        # Créer une nouvelle frame pour l'écran d'inscription
        registration_frame = ttk.Frame(self.root)

        # Ajouter une étiquette de titre à la frame
        ttk.Label(registration_frame, text="Inscription", font=("Arial", 16)).pack(pady=10)

        # Ajouter une étiquette et une entrée pour le nom
        ttk.Label(registration_frame, text="Nom").pack()
        lastname_entry = ttk.Entry(registration_frame)
        lastname_entry.pack()

        # Ajouter une étiquette et une entrée pour le prénom
        ttk.Label(registration_frame, text="Prénom").pack()
        name_entry = ttk.Entry(registration_frame)
        name_entry.pack()

        # Ajouter une étiquette et une entrée pour l'e-mail
        ttk.Label(registration_frame, text="Email").pack()
        email_entry = ttk.Entry(registration_frame)
        email_entry.pack()

        # Ajouter une étiquette et une entrée pour le mot de passe
        ttk.Label(registration_frame, text="Mot de passe").pack()
        password_entry = ttk.Entry(registration_frame, show="*")
        password_entry.pack()

        # Ajouter une étiquette et une entrée pour la confirmation du mot de passe
        ttk.Label(registration_frame, text="Confirmer le mot de passe").pack()
        confirm_password_entry = ttk.Entry(registration_frame, show="*")
        confirm_password_entry.pack()

        # Ajouter un bouton d'inscription qui appelle la méthode d'inscription avec les détails saisis
        ttk.Button(registration_frame, text="Inscription",
                   command=lambda: self.register(lastname_entry.get(), name_entry.get(),
                                                 email_entry.get(), password_entry.get(),
                                                 confirm_password_entry.get())).pack(pady=10)

        # Ajouter un bouton de retour qui affiche la frame de bienvenue
        ttk.Button(registration_frame, text="Retour",
                   command=lambda: self.show_frame(self.welcome_frame)).pack(pady=10)

        # Retourner la frame d'inscription complétée
        return registration_frame

    # Valider l'inscription et créer l'utilisateur si valide
    def login(self, lastname_entry, name_entry, password_entry):
        # Obtenir le nom d'utilisateur et le mot de passe saisis
        lastname_entre = lastname_entry.get()
        name_entre = name_entry.get()
        mot_de_passe_entre = password_entry.get()

        # Valider les détails de connexion
        if not Validator.validate_login(lastname_entre, name_entre, mot_de_passe_entre):
            # Afficher un message d'erreur si la validation échoue
            return
        pseudo = (lastname_entre, name_entre)
        transactions = show_transactions(lastname_entre, name_entre)
        # Si la validation réussit, procéder à la création de la frame principale
        self.root.withdraw()
        self.create_main_frame(pseudo, transactions)

    # Valider l'inscription et créer l'utilisateur si valide
    def register(self, lastname, name, email, password, confirm_password):
        # Valider les détails d'inscription
        if not Validator.validate_registration(lastname, name, email, password, confirm_password):
            return

        # Si la validation réussit, créer un nouvel utilisateur
        create_user(lastname, name, email, password)

        # Afficher un message de succès à l'utilisateur
        msgbox.showinfo("Succès", "Inscription réussie. Vous pouvez maintenant vous connecter.")

        # Afficher la frame de connexion
        self.show_frame(self.login_frame)

    # Afficher les transactions dans un tableau
    @staticmethod
    def show_transactions_table(info_frame, headers, transactions):
        # Afficher les transactions dans un format de tableau
        for idx, transaction in enumerate(transactions):
            for col, value in enumerate(transaction):
                label = ttk.Label(info_frame, text=value, font=("Verdana", 10), background="#36393e",
                                  foreground="white")

                # Changer la couleur en fonction du signe du montant
                if col == 2:  # Supposant que montant est à l'index 2 dans la liste des transactions
                    montant = float(value)
                    if montant > 0:
                        label.config(foreground="green")
                    elif montant < 0:
                        label.config(foreground="red")

                label.grid(row=idx + 2, column=col, sticky="ew", padx=5, pady=5)

        # Ajouter un séparateur après les transactions
        ttk.Separator(info_frame, orient="horizontal").grid(row=len(transactions) + 2, columnspan=len(headers),
                                                            sticky="ew", pady=5)

    # Déconnexion de l'utilisateur
    def disconnect(self):
        # Fermer la fenêtre principale
        self.main_frame.destroy()

    # Créer et afficher la frame principale
    def create_main_frame(self, pseudo, transactions):
        lastname, name = pseudo

        # Créer une nouvelle fenêtre supérieure pour la frame principale
        self.main_frame = tk.Toplevel(self.root)
        self.main_frame.title("Bank")

        # Définir la couleur de fond de la frame principale
        self.main_frame.configure(bg="#282b30")

        # Charger l'image de fond
        self.background_image = tk.PhotoImage(file="assets/pattern.png")
        # Créer une étiquette pour contenir l'image de fond
        background_label = ttk.Label(self.main_frame, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Créer un nouveau cadre pour contenir tous les éléments
        main_container = tk.Frame(self.main_frame, background="#282b30")
        main_container.pack(fill="both", expand=True, padx=20, pady=20)  # Ajout de rembourrage

        # Ajouter une étiquette pour afficher le nom d'utilisateur
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

        # Créer un nouveau cadre pour afficher des informations supplémentaires
        info_frame = tk.Frame(main_container, background="#36393e")
        info_frame.pack(side=tk.TOP, padx=10, pady=10, fill="both", expand=True)  # Ajout de remplissage et d'expansion

        # En-têtes pour les colonnes
        headers = ["Nom", "Description", "Montant", "Type", "Date"]

        def sort_transactions(col_index):
            if col_index != 1:  # Ne pas trier si l'index de colonne correspond à la colonne Description
                # Effacer les lignes de transaction existantes dans info_frame
                for widget in info_frame.winfo_children():
                    if isinstance(widget, ttk.Label):
                        widget.destroy()

                sorted_transactions = sorted(transactions, key=lambda x: x[col_index])
                self.show_transactions_table(info_frame, headers, sorted_transactions)

        # Créer des en-têtes cliquables
        for col, header in enumerate(headers):
            ttk.Button(info_frame, text=header, command=lambda col_index=col: sort_transactions(col_index)).grid(
                row=0, column=col, padx=5, pady=5, sticky="ew")  # Ajout de collant

        # Afficher le tableau de transactions initial
        self.show_transactions_table(info_frame, headers, transactions)

        # Créer et afficher le graphique des dépenses par mois
        self.create_graph(transactions)

    # Créer le graphique des dépenses par mois
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
        plt.savefig('assets/expenses_by_month_graph.png')
        # Afficher le graphique
        plt.show()
