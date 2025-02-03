import customtkinter as ctk
import os

class ImageLable(ctk.CTkLabel):
    def __init__(self, ch_master: object, **kwargs):
        ctk.CTkLabel.__init__(
            self,
            master= ch_master,
            **kwargs
        )
    def load_image(self):
        try:
            pass
        except Exception as exception:
            print(f'Error: {str(exception)}')

def show_image():
    pass