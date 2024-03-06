import modules.screen as scr
import modules.jsonfiles as file


#Añadir productos

def add_products():
    isaddproduct = True
    while isaddproduct:
        scr.clean_screen()
        file.check_file('productos.json')
        productos_data = file.load_file('productos.json')
        id_product = input('Ingrese el ID del producto: ')
        product = {
            'id' : id_product,
            'nombre' : input('Ingrese el nombre del producto: '),
            'valor unitario' : input('Ingrese el valor unitario del producto: '),
            'stockmin' : input('Ingrese el stock minimo del producto: '),
            'stockmax' : input('Ingrese el stock maximo del producto: '),
        
        }
        scr.clean_screen()

        productos_data.update({id_product : product})
        file.update_file('productos.json', productos_data)
        print('Producto registrado exitosamente')
        
        while True:
            scr.clean_screen()
            yes_or_not = input('¿Desea ingresar otro producto? s(si) - n(no)').upper()
            if yes_or_not == 'S':
                break
            elif yes_or_not == 'N':
                isaddproduct = False
                break