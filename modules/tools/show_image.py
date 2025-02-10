import customtkinter as ctk
import os
import PIL.Image
from tkinter import TOP, BOTTOM, BOTH, Y

class ImageLable(ctk.CTkLabel):
    def __init__(self, ch_master: ctk.CTkFrame, path_file: str, **kwargs):
        self.PATH_FILE = path_file
        
        self.WIDTH = int(ch_master._current_width * 0.9)
        self.HEIGHT = int(ch_master._current_height * 0.9)
        
        ctk.CTkLabel.__init__(
            self,
            master= ch_master,
            image= self.load_image(),
            text= '',
            **kwargs
        )
    #
    def load_image(self) -> ctk.CTkImage | None:
        # (image.width, image.height) -> (1024, 800)
        try:
            image = PIL.Image.open(fp= self.PATH_FILE)
            return ctk.CTkImage(
                light_image = image,
                size= self.image_size(image = image)
            )
            # if image.width < self.WIDTH * 0.9 and image.height < self.HEIGHT * 0.9:
            #     return (image.width, image.height)
            # else:
            #     return (self.WIDTH * 0.9, self.HEIGHT * 0.9)
        except Exception as exception:
            print(f'Error: {str(exception)}')
            return None 
    #
    def image_size(self, image: PIL.Image) -> tuple[int, int]:
        # Перевіряємо, що картинка квадратна 
        if image.width == image.height:
            if image.width < self.WIDTH and image.height < self.HEIGHT:
                return (image.width, image.height) # повертаємо незмінний розмір картинки
            elif image.width >= self.WIDTH and image.height >= self.HEIGHT:
                return (self.HEIGHT, self.HEIGHT) # повертаємо новий розмір для зображення, який будується по найменшій стороні dashboard
            else:
                return (self.HEIGHT, self.HEIGHT)
        # Якщо картинка прямокутна
        else:
            if image.width < self.WIDTH and image.height < self.HEIGHT:
                return (image.width, image.height) # повертаємо незмінний розмір картинки
            elif image.width >= self.WIDTH and image.height >= self.HEIGHT:
                return (self.WIDTH, self.HEIGHT) # повертаємо новий розмір для зображення, який будується по розмірам dashboard
            else:
                return (self.WIDTH, self.HEIGHT)

def show_image(button_name: str, frame: ctk.CTkFrame, list_images: list[ImageLable]):
    list_frame = frame.winfo_children()
    for image in list_frame:
        if isinstance(image, ImageLable):
            image.pack_forget()

    for image in list_images:
        if image.PATH_FILE.split('/')[-1] == button_name:
            image.pack(anchor= 'center')

            
    
    