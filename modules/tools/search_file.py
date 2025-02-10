import tkinter.filedialog as filedialog
import customtkinter as ctk
import colorama
from ..gui.app_button import AppButton
from tkinter import Tk, RIGHT, BOTH, RAISED, TOP
from .show_image import ImageLable, show_image

list_image = []
# list_button = []

colorama.init(autoreset= True)
YELLOW = colorama.Fore.YELLOW
GREEN = colorama.Fore.GREEN


def search_file(parent: ctk.CTk, buttons_parent: ctk.CTkFrame | ctk.CTkScrollableFrame, dashboard: ctk.CTkFrame):
    
    list_files = filedialog.askopenfilenames(
        initialdir= '/',
        parent= parent,
        filetypes= [('image files', ['*.png', '*.jpg', '*.bmp', '*.svg', '*.ico', '*.jpeg'])],
        title= 'Search for files'
    )
    print()
    for path_file in list_files:
        # Приклад для одного файлу із списку list_files
        # path_file -> '/Users/worlditacademy/Downloads/worldIT_LOGO.ico'
        # path_file.split("/") -> ['', 'Users', 'worlditacademy', 'Downloads', 'worldIT_LOGO.ico']
        name_file = path_file.split("/")[-1] # -> worldIT_LOGO.ico
        file_type = name_file.split(".")[-1]
        
        # Створення кнопки з назвою файла із розширенням
        button = AppButton(
            ch_master= buttons_parent,
            text_button= f"{name_file[0:12]}...  .{file_type}",
            function= lambda name_button = name_file : show_image(button_name= name_button, frame= dashboard, list_images= list_image)
        )
        image = ImageLable(
            ch_master= dashboard,
            path_file= path_file
        )
        # list_button.append(button)
        list_image.append(image)
        
        # Задаємо параметри розташування кнопки у Explorer
        button.pack(padx= 30, pady=10, anchor = 'w')
        
        print(f'{GREEN}File: -> {YELLOW}{path_file}')
        
    print()
    

