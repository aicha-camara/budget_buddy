import re  # Importation du module re pour les expressions régulières
import tkinter.messagebox as msgbox  # Importation de la boîte de message de tkinter en tant que msgbox
from database import check_user  # Importation de la fonction check_user depuis le module database

# Définition des messages d'erreur en tant que constantes
ERROR_PASSWORD_MISMATCH = "Les mots de passe ne correspondent pas"
ERROR_INVALID_EMAIL = "L'email n'est pas valide"
ERROR_USERNAME_TAKEN = "Un utilisateur avec ce nom d'utilisateur ou email existe déjà"
ERROR_INVALID_LOGIN = "Nom d'utilisateur ou mot de passe invalide"

class Validator:
    @staticmethod  # Utilisé pour éviter de créer une instance de la classe
    def validate_registration(lastname, name, email, password, confirm_password):
        if password != confirm_password:  # Vérifier si les mots de passe correspondent
            msgbox.showerror("Erreur", ERROR_PASSWORD_MISMATCH)
            return False
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Vérifier si l'email est valide en utilisant regex
            msgbox.showerror("Erreur", ERROR_INVALID_EMAIL)
            return False
        # Vérification si le nom et le prénom sont déjà utilisés
        user = check_user(lastname, name, password)
        if user:
            msgbox.showerror("Erreur", ERROR_USERNAME_TAKEN)
            return False
        # Vérification de la complexité du mot de passe
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10,}$", password):
            msgbox.showerror("Erreur", "Le mot de passe doit contenir au moins une majuscule, une minuscule, "
                                       "un caractère spécial, un chiffre et doit avoir au minimum dix caractères.")
            return False
        return True

    @staticmethod  # Utilisé pour éviter de créer une instance de la classe
    def validate_login(lastname, name, password):
        user = check_user(lastname, name, password)
        if not user:  # Vérifier si l'utilisateur existe
            msgbox.showerror("Erreur", ERROR_INVALID_LOGIN)
            return False
        return True
