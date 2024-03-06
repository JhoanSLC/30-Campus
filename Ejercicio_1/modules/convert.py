import modules.screen as scr




#Peso a dolar
def peso_a_dolar() -> float:
    scr.clean_screen()
    while True:
        try:
            peso = float(input('Ingrese el valor de pesos a convertir en dolar (solo números): '))
            if peso <= 0:
                print('Digite un valor positivo: ')
                scr.pause_screen()
                peso_a_dolar()
            break
        except:
            print('Por favor digite un valor correcto')
            scr.pause_screen()
    
    
    
