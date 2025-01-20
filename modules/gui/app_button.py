import os
import customtkinter as ctk
from PIL import Image

class AppButton(ctk.CTkButton):
    def __init__(self, ch_master: object, name_icon: str, **kwargs):
        self.NAME_ICON = name_icon
        self.MASTER = ch_master
        ctk.CTkButton.__init__(
            self,
            master = ch_master,
            text= '',
            width= self.MASTER._current_height * 0.7,
            height= self.MASTER._current_height * 0.7,
            image= self.load_image(),
            **kwargs
        )
    def load_image(self):
        PATH = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'static', 'icons', self.NAME_ICON))
        return ctk.CTkImage(
            light_image= Image.open(PATH),
            size= (self.MASTER._current_height * 0.7, self.MASTER._current_height * 0.7)
        )

