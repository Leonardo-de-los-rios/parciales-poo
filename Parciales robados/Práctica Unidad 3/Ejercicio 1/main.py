from claseManejaLibros import ManejaLibros

from claseMenu import Menu

if __name__=='__main__':
    unManejaLibros=ManejaLibros()
    unManejaLibros.leerArchivo()
    bandera=True
    while bandera:
        menu=Menu()
        opc=menu.menuOpciones()
        if opc == 1:
            idLibro=input('Ingresar ID del libro: ')
            try:
                idLibro=int(idLibro)
                unManejaLibros.buscarLibro(idLibro)
            except:
                print('ID no válido.')

        elif opc == 2:
            palabra=input('Ingrese la palabra: ')
            unManejaLibros.buscarPalabra(palabra)
        elif opc == 0:
            bandera=False