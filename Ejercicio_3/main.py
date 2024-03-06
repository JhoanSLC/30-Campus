"""
Elabore un programa en Python que permita registrar los productos de una
Tienda de viveres. La información se debe almacenar en un archivo JSON. La
Información de los productos es la siguiente (20ptos):

id
nombre
valorUnitario
stockmin
stockmax
valorUnitario

"""
import modules.menus as menu
import modules.products as prod

if __name__ == '__main__':
    isapprunning = True
    while isapprunning:
        prod.scr.clean_screen()
        op = menu.main_menu()
        if op == '1':
            prod.add_products()
        if op == '2':
            isapprunning = False
        