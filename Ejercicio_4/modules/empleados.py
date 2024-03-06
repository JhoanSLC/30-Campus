import modules.jsonfiles as file
import modules.screen as scr

#Añadir empleado
def add_employee():
    scr.clean_screen
    isaddemployee = True
    while isaddemployee:
        file.check_file('empleados.json')
        filedata = file.read_file('empleados.json')
        scr.clean_screen()
        while True:
            try:
                id = int(input('Ingrese el ID del empleado: '))
                id = str(id)
                if id in filedata.keys():
                    print('Este empleado ya se encuentra registrado')
                    scr.pause_screen()
                    add_employee()
                break
            except:
                print('Ingrese un ID valido')
                scr.pause_screen
        employee = {
                'id' : id,
                'nombre' : input('Ingrese el nombre del empleado: '),
                'cargo' : '',
                'salario' : 0.0,
                'colilla de pagos' : {}
        }
        while True:
            scr.clean_screen()
            wichjob = input('Seleccione el cargo del empleado\n1. Almacenista\n2. Jefe IT\n3. Administrador\n4. Mensajero\n5. Gerente\n')
            if wichjob == '1':
                employee['cargo'] = 'Almacenista'
                break
            if wichjob == '2':
                employee['cargo'] = 'Jefe IT'
                break
            if wichjob == '3':
                employee['cargo'] = 'Administrador'
                break
            if wichjob == '4':
                employee['cargo'] = 'Mensajero'
                break
            if wichjob == '5':
                employee['cargo'] = 'Gerente'
                break
        while True:
            scr.clean_screen()
            try:
                salario = float(input('Ingrese el salario base del empleado: '))
                employee['salario'] = salario
                break
            except:
                print('Ingrese un valor correcto')
                scr.pause_screen()
        filedata.update({id : employee})
        file.update_file('empleados.json', filedata)
        scr.clean_screen
        print('Empleado agregado exitosamente')
        while True:
            yes_or_not = input('¿Desea agregar otro empleado? s(sí) - n(no): ').upper()
            if yes_or_not == 'S':
                break
            elif yes_or_not == 'N':
                isaddemployee = False
                break
