import os 
import sys


#Limpiar pantalla según el os
def clean_screen():
    if sys.platform == 'linux':
        os.system('clear')
    elif sys.platform == 'windows':
        os.system('cls')

#Pausar pantalla según el os
def pause_screen():
    if sys.platform == 'linux':
        input('Presione cualquier tecla para continuar . . . ')
    if sys.platform == 'windows':
        os.system('pause')