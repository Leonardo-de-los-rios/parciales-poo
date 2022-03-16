class Reparacion:
    __idReparacion=0

    def __init__(self,idReparacion=0):
        assert isinstance(idReparacion,int)
        self.__idReparacion=idReparacion


    def getIdReparacion(self):
        return self.__idReparacion