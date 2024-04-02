import mysql.connector


def __init__(self, host, user, password, database):
    self.connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="za9?-U5zwD4-6#L",
        database="budget_app"
    )
    self.curseur = self.connexion.cursor()

def check_user(lastname, name, password):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="za9?-U5zwD4-6#L",
        database="budget_app"
    )
    curseur = connexion.cursor()

    requete = "SELECT * FROM id WHERE nom = %s AND prenom= %s AND mots_de_passe = %s"
    valeurs = (lastname, name, password)
    curseur.execute(requete, valeurs)
    user = curseur.fetchone()
    curseur.close()
    connexion.close()
    return user

def get_username(self):
    requete = "SELECT pseudo FROM id WHERE (pseudo = ? OR email = ?)"
    self.curseur.execute(requete)
    username = self.curseur.fetchall()
    return username[0]
def create_user(lastname, name, email, password):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="za9?-U5zwD4-6#L",
        database="budget_app"
    )
    curseur = connexion.cursor()

    requete = "INSERT INTO id (nom, prenom, email, mots_de_passe) VALUES (%s,%s, %s, %s)"
    valeurs = (lastname, name, email, password)
    curseur.execute(requete, valeurs)

    connexion.commit()  # Valider les modifications dans la base de données

    curseur.close()
    connexion.close()

def show_transactions(lastname, name):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="za9?-U5zwD4-6#L",  # Modifier avec votre mot de passe
        database="budget_app"
    )
    curseur = connexion.cursor()

    requete = ("SELECT nom, description, montant, type, date FROM transactions WHERE utilisateur_id=(SELECT id FROM id "
               "WHERE nom=%s AND prenom=%s)")
    valeurs = (lastname, name)
    curseur.execute(requete, valeurs)

    transactions = []
    for row in curseur.fetchall():
        transactions.append(row)

    curseur.close()
    connexion.close()

    return transactions
