import re
import tkinter.messagebox as msgbox

from database import check_user

# Define error messages as constants
ERROR_PASSWORD_MISMATCH = "Les mots de passe ne correspondent pas"
ERROR_INVALID_EMAIL = "L'email n'est pas valide"
ERROR_USERNAME_TAKEN = "Un utilisateur avec ce nom d'utilisateur ou email existe déjà"
ERROR_INVALID_LOGIN = "Nom d'utilisateur ou mot de passe invalide"
class Validator:
    @staticmethod  # Used to avoid creating an instance of the class
    def validate_registration(username, email, password, confirm_password):
        if password != confirm_password:  # Check if passwords match
            msgbox.showerror("Erreur", ERROR_PASSWORD_MISMATCH)
            return False
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Check if email is valid using regex
            msgbox.showerror("Erreur", ERROR_INVALID_EMAIL)
            return False
        if username.lower() == "admin":  # Check if username is 'admin'
            msgbox.showerror("Erreur", "Le nom d'utilisateur 'admin' n'est pas autorisé")
            return False
        user = check_user(username, password)  # Check if username is taken
        if user:
            user = check_user(email, password)  # Check if email is taken
            if user:
                msgbox.showerror("Erreur", ERROR_USERNAME_TAKEN)
                return False
                # Check if password meets complexity requirements
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10,}$", password):
            msgbox.showerror("Erreur","Le mot de passe doit contenir au moins une majuscule, une minuscule, un caractère spécial, un chiffre et doit avoir au minimum dix caractères.")
            return False
        return True

    @staticmethod  # Used to avoid creating an instance of the class
    def validate_login(username, password):
        user = check_user(username, password)
        if not user:  # Check if user exists
            msgbox.showerror("Erreur", ERROR_INVALID_LOGIN)
            return False
        return True
