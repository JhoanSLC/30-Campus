import modules.screen as scr


#Convert
def convert(op):
    peso = 0.0
    dolar = 3944.0 #en pesos
    euro = 4279.0 #en pesos
    yen = 26.30 #En pesos
    scr.clean_screen()
    moneda_1 = ''
    moneda_2 = ''
    if op == '1':
        moneda_1 = 'peso'
        moneda_2 = 'dolar'
    if op == '2':
        moneda_1 = 'peso'
        moneda_2 = 'euro'
    if op == '3':
        moneda_1 = 'euro'
        moneda_2 = 'peso'
    if op == '4':
        moneda_1 = 'peso'
        moneda_2 = 'yen'
    scr.clean_screen()
    while True:
        try:
            peso = float(input(f'Ingrese el valor de {moneda_1} a convertir en {moneda_2} (solo números): '))
            if peso <= 0:
                print('Digite un valor positivo: ')
                scr.pause_screen()
                convert()
            break
        except:
            print('Por favor digite un valor correcto')
            scr.pause_screen()
    if op == '1':
        dolar_value = 0
        





    
    
    
