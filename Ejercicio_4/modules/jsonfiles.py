import os 
import modules.screen as scr
import json

BASE = 'data/'

#Chequear si el archivo existe y si no existe crearlo
def check_file(file : str):
    if not os.path.isfile(BASE+file):
        with open(BASE+file, 'w') as create:
            json.dump({}, create, indent = 4)

#Cargar contenido del archivo json a variable python
def read_file(file : str) -> dict:
    with open(BASE+file, 'r') as read:
        info = json.load(read)
    return info

#Actualizar contenido de archivo json
def update_file(file : str, data):
    with open(BASE+file, 'w+') as update:
        json.dump(data, update, indent = 4)
        
