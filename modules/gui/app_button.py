r'''
    У модулі розміщено інструкцію клас (AppButton), ціль якого створювати та налаштовувати кнопки 
    у графічному інтерфейсі будь якого застосунку
    
    Модулі:
        - `customtkinter` - для створення вікна кнопки
        - `PIL` - для завантаження зображення з папки static/icons
        - `os` - для роботи з папками та файлами
    
    Приклад застосування: 
    >>> app_button = AppButton(ch_master=self, name_icon='edit.png')
'''
import os
import customtkinter as ctk
from PIL import Image

class AppButton(ctk.CTkButton):
    r"""
        Конструктор (__init__) створює кнопку з завантаженим зображенням з папки static/icons
        
        parameter :mod:`ch_master` - у параметрі вказуємо до якого вікна (фрейму) додається кнопка;
        parameter :mod:`name_icon` - у параметрі вказуємо назву зображення з папки static/icons;
        parameter :mod:`size_side` - у параметрі вказуємо розмір сторони зображення в пікселях;
        
        Методи:
            :mod:`load_image` - завантажує зображення з папки static/icons з заданим розміром;
            :mod:`os.path.abspath` - для роботи з папками та файлами;
        Класи:
            :mod:`ctk.CTkButton` - для створення кнопки;
            :mod:`PIL.Image.open` - відкриває зображення та повертає значення до класу CTkImage;
            :mod:`ctk.CTkImage` - задає формат зображенню в CTkImage для відображення у графічному інтерфейсі застосунку
        
    """
    def __init__(self, ch_master: object, name_icon: str, size_side: float, **kwargs):
        self.NAME_ICON = name_icon
        self.SIZE = (int(size_side), int(size_side))
        ctk.CTkButton.__init__(
            self,
            master = ch_master,
            text= '',
            width=  int(size_side),
            height= int(size_side),
            image= self.load_image(),
            **kwargs
        )
    def load_image(self):
        PATH = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'static', 'icons', self.NAME_ICON))
        return ctk.CTkImage(
            light_image= Image.open(PATH),
            size= self.SIZE
        )

