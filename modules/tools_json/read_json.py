import json
import os

def read_json(file_name: str):
    try:
        path_to_file = os.path.abspath(__file__ + f'/../../../static/json/{file_name}')
        with open(file= path_to_file, mode= 'r') as file:
            return json.load(file)

    except Exception as exception:
        print(f'\nError reading file: {exception}\n')


print(read_json(file_name= 'config.json'))