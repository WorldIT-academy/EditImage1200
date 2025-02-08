import customtkinter as ctk
import os
import PIL.Image
from tkinter import TOP, BOTTOM, BOTH, Y

class ImageLable(ctk.CTkLabel):
    def __init__(self, ch_master: ctk.CTkFrame, path_file: str, **kwargs):
        self.PATH_FILE = path_file
        
        self.WIDTH = ch_master._current_width
        self.HEIGHT = ch_master._current_height
        
        ctk.CTkLabel.__init__(
            self,
            master= ch_master,
            image= self.load_image(),
            text= '',
            **kwargs
        )
    def load_image(self):
        # (image.width, image.height) -> (1024, 800)
        try:
            image = PIL.Image.open(fp= self.PATH_FILE)
            return ctk.CTkImage(
                light_image = image,
                size= (image.width, image.height) if image.width < self.WIDTH * 0.9 and image.height < self.HEIGHT * 0.9 else (self.WIDTH *0.9, self.HEIGHT *0.9)
            )
            # if image.width < self.WIDTH * 0.9 and image.height < self.HEIGHT * 0.9:
            #     return (image.width, image.height)
            # else:
            #     return (self.WIDTH * 0.9, self.HEIGHT * 0.9)
        except Exception as exception:
            print(f'Error: {str(exception)}')

def show_image(image: ImageLable):
    image.pack(anchor= 'center')
    