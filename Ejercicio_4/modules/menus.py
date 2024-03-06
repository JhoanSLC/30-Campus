import modules.screen as scr



#Dibujar menu principal
def main_menu():
    scr.clean_screen
    titulo = """
        +++++++++++++++++++++++++++++++++
        + REGISTRO DE EMPLEADOS Y PAGOS +
        +++++++++++++++++++++++++++++++++

    """
    print(titulo)
    print('')
    print('Ingrese el número correspondiente a la opción que desea realizar')
    op = input('1. Registrar empleado\n2. Agregar colilla de pago\n3. Ver total pagado por concepto de nomina\n4. Consultar colilla de pago\n5. Salir\n')
    return op