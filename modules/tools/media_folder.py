import os 
import colorama

colorama.init()
def create_media_folder():
    try:
        media_folder_path = os.path.abspath(__file__ + f'/../../../media')
        os.mkdir(path= media_folder_path )
        os.mkdir(path= os.path.join(media_folder_path, 'images'))
        os.mkdir(path= os.path.join(media_folder_path, 'images/dowloads'))
        os.mkdir(path= os.path.join(media_folder_path, 'images/edits'))
    except FileExistsError:
        print(f'\n{colorama.Fore.YELLOW}⚠️ Folder already exists ⚠️{colorama.Style.RESET_ALL}')

create_media_folder()