import modules.jsonfiles as file
import modules.screen as scr

colillanum = 0
valorextra = 5500

#Calcular valor a pagar para un empleado
def calcular_pago():
    global colillanum
    global valorextra
    isthisrunning = True
    while isthisrunning:
        scr.clean_screen()
        file.check_file('empleados.json')
        data_empleados = file.read_file('empleados.json')
        id_a_calcular = input('Ingrese el ID del empleado al que desea calcular valor total a pagar: ')
        if id_a_calcular in data_empleados.keys():
            salario_base = data_empleados[id_a_calcular].get('salario')
            valor_dia = round(salario_base / 30, 2)
            while True:
                scr.clean_screen()
                try: 
                    valores_a_pagar = {
                        'dias trabajados' : float(input('Ingrese los días trabajados: ')),
                        'horas extra' : float(input('Ingrese las horas extra trabajadas: ')),
                        'valor dia' : valor_dia,
                        'descuento x cafeteria' : float(input('Ingrese el valor a descontar por cafetería: ')),
                        'cuota prestamo' : float(input('Ingrese el valor de cuota de prestamos a descontar: '))
                    }
                    break
                except: 
                    print('Por favor digite un valor válido')
                    scr.pause_screen()
            scr.clean_screen()
            total_pago_dias = (valor_dia * valores_a_pagar.get('dias trabajados'))
            total_pago_horas = (valor_dia / 8) * valores_a_pagar.get('horas extra')
            descuentocafe = valores_a_pagar.get('descuento x cafeteria')
            cuotaprestamo = valores_a_pagar.get('cuota prestamo')
            suma_dias_horas = (total_pago_dias + total_pago_horas)
            total_a_pagar = (suma_dias_horas - (descuentocafe) - (cuotaprestamo))
            colilla = {
                    'mes pagado' : input('Ingrese el mes pagado: '),
                    'fecha pago' : '',
                    'sueldo base' : salario_base,
                    'total horas extra' : total_pago_horas,
                    'cuota prestamo' : cuotaprestamo,
                    'descuento por cafeteria' : descuentocafe,
                    'total a pagar' : total_a_pagar,
            }
            scr.clean_screen()
            dd = input('Ingrese el día en que se realizó el pago: ')
            mm = input('Ingrese el mes en que se realiza el pago: ')
            yy = input('Ingrese el año en que se realiza el pago: ')
            colilla['fecha pago'] = f'{dd}/{mm}/{yy}'
            scr.clean_screen()
            data_empleados[id_a_calcular]['colilla de pagos'].update({colillanum : colilla})
            file.update_file('empleados.json', data_empleados)
            colillanum += 1
            print('Colilla actualizada con exito, dirijase a ver colilla para verificar')
            scr.pause_screen()
            while True:
                yes_or_not = input('¿Desea agregar otra colilla de pago? s(sí) - n(no): ').upper()
                if yes_or_not == 'S':
                    break
                elif yes_or_not == 'N':
                    isthisrunning = False
                    break

            


        else:
            print('El empleado no se encuentra registrado')
            scr.pause_screen()
            

#Calcular total pagado por nomina
def total_nomina():
    isthisrunning = True
    while isthisrunning:
        scr.clean_screen()
        file.check_file('empleados.json')
        data_empleados = file.read_file('empleados.json')
        pagos = []
        for key, value in data_empleados.items():
            for key, v in data_empleados[key]['colilla de pagos'].items():
                if key == 'colilla de pagos':
                    pagos.append(v)

        suma_total = sum(pagos)
        print(f'EL total pagado por nomina es: {suma_total}')
        scr.pause_screen()
        break
       