"""

"""
import modules.menus as menu
import modules.empleados as emp
import modules.pagos as pay

if __name__ == '__main__':
    isapprunning = True
    while isapprunning:
        emp.scr.clean_screen()
        op = menu.main_menu()
        #Añadir empleado
        if op == '1':
            emp.add_employee()
        #Calcular valor a pagar
        if op == '2':
            pay.calcular_pago()
        #Total pagado por nomina
        if op == '3':
            pay.total_nomina()
        #Colilla de pago
        if op == '4':
            pass
        #Salir 
        if op == '5':
            isapprunning = False

