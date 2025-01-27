import tkinter.filedialog as filedialog
import customtkinter as ctk

def search_file():
    list_files = filedialog.askopenfilenames(
        initialdir= '/',
        parent= None,
        filetypes= [('image files', ['*.png', '*.jpg'])],
        title= 'Search for files'
    )
    print(list_files)

