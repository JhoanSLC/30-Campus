"""
2. Elabore un programa en Python que permita leer la información de un usuario
Y la almacene en un diccionario. La información del usuario es la siguiente(15 ptos):
id
nombres
apellidos
ubicación
dirección
ciudad
longitud
latitud
email
edad
ocupación
"""
import modules.users as users

if __name__ == '__main__':
    isapprunning = True
    usersdict = {}
    while isapprunning:
        users.scr.clean_screen()
        print('Ingrese el número correspondiente a la acción que desea realizar')
        print('')
        op = input('1. Registrar usuario\n2. Mostrar usuarios\n3. Salir\n')

        if op == '1':
            users.scr.clean_screen()
            users.add_users(usersdict)
        if op == '2':
            users.scr.clean_screen()
            users.print_users(usersdict)
        if op == '3':
            isapprunning = False
            break
