from claseProducto import Producto

from claseReparacion import Reparacion

class Recepcion(Reparacion):
    __fechaRecepcion=''
    __producto=None

    def __init__(self,idReparacion=0,fechaRecepcion='',producto=None):
        assert isinstance(fechaRecepcion,str)
        super().__init__(idReparacion)
        self.__fechaRecepcion = fechaRecepcion
        self.__producto=Producto
    
    def addProducto(self,unProducto):
        assert isinstance(unProducto,Producto)
        self.__producto=unProducto

    