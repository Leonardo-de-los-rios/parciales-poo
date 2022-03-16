from claseManejadorFacultades import ManejadorFacultades

from claseManejadorCarreras import ManejadorCarreras

def test():
    unManejaFacultades=ManejadorFacultades()
    unManejaFacultades.leerArchivo()
    
    unManejaCarreras=ManejadorCarreras()
    unManejaCarreras.leerArchivo(unManejaFacultades)
    print(unManejaFacultades)


if __name__=='__main__':
    test()