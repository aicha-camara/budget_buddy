class Application:
    def __init__(self, numero_de_compte, nom, prenom, solde, description, type, montant, decouvert=True):
        self.__numero_de_compte = numero_de_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = -100

        self.__description = description
        self.__montant = montant
        self.__type = type
        self.__historique = []
        self.__historique_virements = []

    def get_numero_de_compte(self):
        return self.__numero_de_compte

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_solde(self):
        return self.__solde

    def get_decouvert(self):
        return self.__decouvert

    def set_solde(self, nouveau_solde):
        self.__solde = nouveau_solde
        return self.__solde

    def afficher(self):
        info_compte = (
            f"Numero de compte = {self.__numero_de_compte}\n"
            f"Nom = {self.__nom}\n"
            f"Prenom = {self.__prenom}\n"
        )
        return info_compte

    def afficherSolde(self):
        info_solde = f"Le solde de {self.__nom} = {self.__solde} €\n"
        return info_solde

    def versement(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Vous avez versé : {montant}€\nLe nouveau solde de {self.__nom} est de :\n{self.afficherSolde()}")
        return self.__solde

    def agios(self):
        if self.__solde < 0:
            frais = 5
            self.__solde -= frais
            print(f"Des frais supplémentaires de {frais} ont été appliqués dans votre compte. Raison : Votre solde est en négatif.\n")
        return self.__solde

    def virement(self, montant, destinateur):
        if montant > 0 and self.__solde - montant >= -self.__decouvert:
            self.__solde -= montant
            destinateur.__solde += montant
            description = input("Entrez la description du virement : ")
            type_virement = input("Entrez le type du virement (ex: chèque, virement en ligne, etc.) : ")
            virement_info = f"De {self.__nom} à {destinateur.__nom}: montant={montant}, description={description}, type={type_virement}"
            self.__historique_virements.append(virement_info)
            print(
                f"{self.__nom} a fait un virement de {montant}€ à {destinateur.__nom}\nLe nouveau solde de {self.__nom} est de :\n{self.afficherSolde()} et le nouveau solde de {destinateur.__nom} est de {destinateur.afficherSolde()} ")
        else:
            print(
                f"Le montant de {montant}€ ne peut pas être valide car vous dépassez le découvert ou le montant est invalide")
        return self.__solde

    def afficher_historique_virements(self):
        if self.__historique_virements:
            print("\nHistorique des virements:")
            for virement in self.__historique_virements:
                print(virement)
        else:
            print("\nAucun virement effectué.")

# Fonction pour afficher le menu
def afficher_menu():
    print("\nMenu:")
    print("1. Afficher les informations du compte")
    print("2. Afficher le solde du compte")
    print("3. Faire un versement")
    print("4. Historique")
    print("5. Faire un virement")
    print("6. Changer de compte")
    print("7. Quitter")

# Programme principal
def choisir_compte():
    print("Choisissez votre compte :")
    print("1. Compte 1 - Jean Dupont")
    print("2. Compte 2 - Sophie Martin")
    choix = input("Entrez le numéro du compte : ")
    if choix == "1":
        return Application("123456", "Dupont", "Jean", 1000, "", "", 0, [])
    elif choix == "2":
        return Application("789012", "Martin", "Sophie", 2000, "Versement", "", 0, [])
    else:
        print("Choix invalide. Veuillez réessayer.")
        return choisir_compte()

def main():
    compte_actuel = choisir_compte()

    continuer = True

    while continuer:
        afficher_menu()
        choix = input("Entrez votre choix : ")

        if choix == "1":
            print(compte_actuel.afficher())
        elif choix == "2":
            print(compte_actuel.afficherSolde())
        elif choix == "3":
            montant = float(input("Entrez le montant du versement : "))
            compte_actuel.versement(montant)
        elif choix == "4":
            compte_actuel.afficher_historique_virements()
        elif choix == "5":
            print("Choisissez le compte destinataire:")
            print("1. Compte 1 - Jean Dupont")
            print("2. Compte 2 - Sophie Martin")
            compte_dest_choice = input("Entrez le numéro du compte destinataire : ")

            # Récupérer le compte destinataire en fonction du choix de l'utilisateur
            compte_dest = None
            if compte_dest_choice == "1":
                compte_dest = choisir_compte()  # Choisir le compte destinataire
            elif compte_dest_choice == "2":
                compte_dest = choisir_compte()  # Choisir le compte destinataire
            else:
                print("Numéro de compte invalide.")

            # Si le compte destinataire est valide, effectuer le virement
            if compte_dest:
                montant = float(input("Entrez le montant du virement : "))
                compte_actuel.virement(montant, compte_dest)
        elif choix == "6":
            compte_actuel = choisir_compte()
            afficher_menu()  # Afficher le menu après le changement de compte
        elif choix == "7":
            continuer = False
            print("Au revoir !")
        else:
            print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()
