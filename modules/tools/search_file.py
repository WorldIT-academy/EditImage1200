import tkinter.filedialog as filedialog
import customtkinter as ctk
import colorama
from ..gui.app_button import AppButton
from tkinter import Tk, RIGHT, BOTH, RAISED

colorama.init(autoreset= True)
YELLOW = colorama.Fore.YELLOW
GREEN = colorama.Fore.GREEN


def search_file(parent: object, buttons_parent: object):
    # list_names_files = []
    list_files = filedialog.askopenfilenames(
        initialdir= '/',
        parent= parent,
        filetypes= [('image files', ['*.png', '*.jpg', '*.bmp', '*.svg', '*.ico', '*.jpeg'])],
        title= 'Search for files'
    )
    print()
    for name_file in list_files:
        # list_names_files.append(name_file.split("/")[-1])
        button = AppButton(
            ch_master= buttons_parent,
            text_button= name_file.split("/")[-1]  
        )
        button.pack(pady=10, expand=False, fill= BOTH, in_= buttons_parent)
        
        print(f'{GREEN}File: -> {YELLOW}{name_file}')
        
    print()
    # print(f'List of names: {GREEN}{list_names_files}')

