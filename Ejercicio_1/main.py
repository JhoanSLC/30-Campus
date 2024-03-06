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
    op = menu.main_menu()
    
    #Peso a dolar
    if op == '1':
        conv.peso_a_dolar()
    #Peso a euros
    if op == '2':
        pass
    #Euro a peso
    if op == '3':
        pass
    #Peso a yen
    if op == '4':
        pass