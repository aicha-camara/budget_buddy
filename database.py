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
