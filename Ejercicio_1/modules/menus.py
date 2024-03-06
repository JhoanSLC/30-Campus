import modules.screen as scr

#Crea el menu principal
def main_menu() -> str:
    optioncorrect = True
    while optioncorrect:
        options = ['1', '2', '3', '4', '5']
        scr.clean_screen()
        titulo = """
            
            +++++++++++++++++++++
            + Convertir monedas +
            +++++++++++++++++++++

        """
        print(titulo)
        print('')
        print('Digite el número correspondiente a la acción que desea realizar')
        op = str(input('1. Convertir pesos a dolares\n2. Convertir pesos a euros\n3. Convertir euros a pesos\n4. Convertir de pesos pesos a yenes\n5. Salir\n'))
        if op in options:
            optioncorrect = False
            return op

        
