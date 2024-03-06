"""
1. Elabore un programa en Python que permita convertir de pesos a dólares, de
pesos a euros, de euros a pesos, de pesos a yenes. (10 ptos)
1 yen = 26.30 pesos
1 dólar = 3944 pesos
1 euro = 4279 pesos

"""
import modules.menus as menu
import modules.convert as conv


if __name__ == '__main__':
    isapprunning = True
    while isapprunning:
        menu.scr.clean_screen()
        op = menu.main_menu()
        
        if op == '5':
            isapprunning = False
            break
        dolar = conv.convert(op)

        
