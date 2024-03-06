import modules.screen as scr
from tabulate import tabulate



#Añadir usuarios
def add_users(users : dict):
    scr.clean_screen()
    add_user = True
    while add_user:
        scr.clean_screen
        user = {
            'id' : 0,
            'nombres' : '',
            'apellidos' : '',
            'ubicación' : {
                    'direccion' : '',
                    'ciudad' : '',
                    'longitud' : 0,
                    'latitud' : 0
            },
            'email' : '',
            'edad' : 0,
            'ocupacion' : '',
        }
        while True:
            scr.clean_screen()
            try:
                id = int(input('Ingrese el ID del usuario a registrar: '))
                id = str(id)
                break
            except ValueError:
                print('Ingrese un valor valido')
                scr.pause_screen()
        user['id'] = id
        user['nombres'] = input('Ingrese el/los nombre/s del usuario: ')
        user['apellidos'] = input('Ingrese el/los apellido/s del usuario: ')
        user['ubicación']['direccion'] = input('Ingrese la dirección del usuario: ')
        user['ubicación']['ciudad'] = input('Ingrese la ciudad donde se encuentra el usuario: ')
        while True:
            scr.clean_screen()
            try:
                long = float(input('Ingrese la longitud de la ubicación del usuario: '))
                long = str(long)
                user['ubicación']['longitud'] = long
                break
            except:
                print('Digite un valor correcto')
                scr.pause_screen
        while True:
            scr.clean_screen()
            try:
                lat = float(input('Ingrese la longitud de la ubicación del usuario: '))
                lat = str(lat)
                user['ubicación']['latitud'] = lat
                break
            except:
                print('Por favor digite un valor correcto')
                scr.pause_screen()
        user['email'] = input('Ingrese el email del usuario: ')
        while True:
            scr.clean_screen()
            try:
                age = int(input('Ingrese la edad del usuario: '))
                age = str(age)
                user['edad'] = age
                break
            except:
                print('Digite una edad correcta')
                scr.pause_screen()
        user['ocupacion']= input('Ingrese la ocupación del usuario: ')
        scr.clean_screen()
        users.update({id : user})
        print('Usuario registrado exitosamente')
        while True:
            scr.clean_screen()
            yes_or_not = input('¿Desea registrar otro usuario? s(sí) - n(no)').upper()
            if yes_or_not == 'S':
                break
            elif yes_or_not == 'N':
                add_user = False
                break
                
#Imprimir usuarios
def print_users(users : dict):
    scr.clean_screen()
    kys = ['id', 'nombres', 'apellidos', 'dirección', 'ciudad', 'longitud', 'latitud', 'email', 'edad', 'ocupación']   
    info = []
    for key, value in users.items():
        for v in value.values():
            if isinstance(v, dict):
                for ks, vs in v.items():
                    info.append(vs)
            else:
                info.append(str(v))
    print(tabulate([info], headers = kys, tablefmt = 'fancy_grid'))
    scr.pause_screen()


                    


