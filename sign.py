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
