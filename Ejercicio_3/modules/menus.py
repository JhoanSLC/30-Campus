import modules.screen as scr


#Dibujar menu principal
def main_menu() -> str:
    scr.clean_screen()
    titulo = """
        +++++++++++++++++++++++++
        + REGISTRO DE PRODUCTOS +
        +++++++++++++++++++++++++
    """
    print(titulo)
    print('')
    print('Ingrese el número correspondiente a la acción que desea realizar')
    op = input('1. Registrar productos\n2. Salir\n')
    return op