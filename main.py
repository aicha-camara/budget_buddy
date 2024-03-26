import tkinter as tk

# Fonction pour gérer un événement
def button_click():
    label.config(text="Bouton cliqué!")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Ma Application Tkinter")

# Création d'un widget Label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

# Création d'un widget Button
button = tk.Button(root, text="Cliquez-moi!", command=button_click)
button.pack(pady=5)

# Boucle principale de la fenêtre
root.mainloop()
