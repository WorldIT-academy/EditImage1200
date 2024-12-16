import customtkinter as ctk
from ..read_json import read_json

class App(ctk.CTk):
    def __init__ (self):
        ctk.CTk.__init__(self)
        
        self.WIDTH = self.winfo_screenwidth()
        self.HEIGHT = self.winfo_screenheight()
        self.geometry('400x300')