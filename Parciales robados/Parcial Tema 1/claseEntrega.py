from claseReparacion import Reparacion

class Entrega(Reparacion):
    __fechaEntrega=''
    __detalle=''
    __monto=0.0

    def __init__(self,idReparacion=0,fechaEntrega='',detalle='',monto=0.0):
        assert isinstance(fechaEntrega,str)
        assert isinstance(detalle,str)
        assert (isinstance(monto,float) or isinstance(monto,int))
        super().__init__(idReparacion)
        self.__fechaEntrega=fechaEntrega
        self.__detalle=detalle
        self.__monto=monto