import mysql.connector


def __init__(self, host, user, password, database):
    self.connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="za9?-U5zwD4-6#L",
        database="myDiscord"
    )
    self.curseur = self.connexion.cursor()

def check_user(username, password):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="za9?-U5zwD4-6#L",
        database="myDiscord"
    )
    curseur = connexion.cursor()

    requete = "SELECT * FROM identifiant WHERE pseudo = %s AND mots_de_passe = %s"
    valeurs = (username, password)
    curseur.execute(requete, valeurs)
    user = curseur.fetchone()
    curseur.close()
    connexion.close()
    return user

def get_username(self):
    requete = "SELECT pseudo FROM identifiant WHERE (pseudo = ? OR email = ?)"
    self.curseur.execute(requete)
    username = self.curseur.fetchall()
    return username[0]

def create_user(username, email, password):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="za9?-U5zwD4-6#L",
        database="myDiscord"
    )
    curseur = connexion.cursor()

    requete = "INSERT INTO identifiant (pseudo, email, mots_de_passe) VALUES (%s, %s, %s)"
    valeurs = (username, email, password)
    curseur.execute(requete, valeurs)

    connexion.commit()  # Valider les modifications dans la base de données

    curseur.close()
    connexion.close()