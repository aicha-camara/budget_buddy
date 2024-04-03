from sign import Frames  # Importation de la classe Frames depuis le module sign
import tkinter as tk  # Importation de tkinter en tant que tk


def main():
    # Initialisation de la fenêtre principale
    root = tk.Tk()
    root.title("Budget")  # Définition du titre de la fenêtre

    # Obtenir la taille de l'écran
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Définir la taille de la fenêtre principale à la moitié de la taille de l'écran
    root.geometry(f"{screen_width // 2}x{screen_height // 2}")

    # Initialisation des cadres
    frames = Frames(root)

    # Afficher le cadre de bienvenue
    frames.show_frame(frames.welcome_frame)

    # Démarrer la boucle d'application
    root.mainloop()


# Point d'entrée du programme
if __name__ == "__main__":
    main()
