import json
import sys
import os



BASE = 'data/'

#Chequear si el archivo existe y si no existe lo crea
def check_file(file : str):
    if not os.path.isfile(BASE+file):
        with open(BASE+file, 'w') as create_file:
            json.dump({}, create_file, indent = 4)  
    else: 
        pass


#Cargar contenido del archivo json
def load_file(file : str):
    with open(BASE+file, 'r') as loadfile:
        data = json.load(loadfile)
    return data

#Actualizar archivo json
#Recibe: nombre del archivo e información a actualizar
def update_file(file : str, info):
    with open(BASE+file, 'w+') as updatefile:
        json.dump(info, updatefile, indent = 4)