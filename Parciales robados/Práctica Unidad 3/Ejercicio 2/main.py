from claseManejadorHelados import ManejadorHelados

from claseManejadorSabores import ManejadorSabores

from claseMenu import Menu

if __name__=='__main__':
    unManejadorSabores=ManejadorSabores()
    unManejadorHelados=ManejadorHelados()
    unManejadorSabores.leerArchivo()
    bandera=True
    while bandera:
        menu=Menu()
        opc=menu.menuOpciones()
        if opc == 1:
            gramos=input('Ingrese los gramos: ')
            try:
                gramos=int(gramos)
                unManejadorHelados.registrarVenta(gramos,unManejadorSabores)
            except:
                print('Error')
        elif opc == 2:
            pass
        elif opc == 3:
            pass
        elif opc == 4:
            pass
        elif opc == 0:
            bandera=False