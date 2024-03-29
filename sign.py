import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import ttk
from database import create_user
from validator import Validator

class Frames:
    def __init__(self, root):
        self.root = root
        self.username = None
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

    def create_welcome_frame(self):
        # Create a new frame for the welcome screen
        welcome_frame = ttk.Frame(self.root)

        # Load the background image
        # self.background_image = tk.PhotoImage(file="pattern.png")

        # Create a label to hold the background image
        # background_label = ttk.Label(welcome_frame, image=self.background_image)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Add a welcome label to the frame
        ttk.Label(welcome_frame, text="Bonjour cher client!", font=("Helvetica", 16)).pack(pady=20)

        # Create a container for the buttons
        button_container = ttk.Frame(welcome_frame)
        button_container.pack(pady=10)

        # Add a login button to the button container
        ttk.Button(button_container, text="Se connecter",
                    command=lambda: self.show_frame(self.login_frame)).pack(side=tk.LEFT, padx=10)

        # Add a registration button to the button container
        ttk.Button(button_container, text="S'inscrire",
                    command=lambda: self.show_frame(self.registration_frame)).pack(side=tk.LEFT, padx=10)

        # Return the completed welcome frame
        return welcome_frame

