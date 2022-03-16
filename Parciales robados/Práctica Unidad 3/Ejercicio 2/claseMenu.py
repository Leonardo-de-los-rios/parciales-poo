class Menu:

    def menuOpciones(self):
        print('1. Registrar venta de helado.')
        print('2. Nombre de los 5 sabores más pedidos.')
        print('3. Gramos vendidos por sabor.')
        print('4. Mostrar sabores vendidos según tamaño de helado.')
        print('0. Salir')
        opcionCorrecta=False
        while opcionCorrecta==False:
            opc=int(input('Ingrese una opción: '))
            if opc in [0,1,2,3,4]:
                opcionCorrecta=True
        return opc