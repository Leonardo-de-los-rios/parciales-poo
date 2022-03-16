class Menu:

    def menuOpciones(self):
        print('1. Buscar Libro por ID.')
        print('2. Buscar Título por palabra.')
        print('0. Salir')
        opcionCorrecta=False
        while opcionCorrecta==False:
            opc=int(input('Ingrese una opción: '))
            if opc in [0,1,2]:
                opcionCorrecta=True
        return opc