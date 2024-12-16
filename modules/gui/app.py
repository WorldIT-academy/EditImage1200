import customtkinter as ctk
from ..read_json import read_json

class App(ctk.CTk):
    def __init__ (self):
        
        self.CONFIG = read_json(fd= 'config.json')
        
        ctk.CTk.__init__(self, fg_color= self.CONFIG['app_fg_color'])
        # отримуємо інформацію ширини екрана нашого комп`ютера
        self.WIDTH = int(self.winfo_screenwidth() * self.CONFIG["app_width"]) 
        # отримуємо інформацію висоти екрана нашого комп`ютера
        self.HEIGHT = int(self.winfo_screenheight() * self.CONFIG["app_height"])
        # задаємо розмiри нашого застосунку
        self.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        # задає загаловок для нашого застосунку
        self.title(self.CONFIG["app_title"])
        
# Створюємо застосунок з назвою app за інструкцією App()
app = App()
