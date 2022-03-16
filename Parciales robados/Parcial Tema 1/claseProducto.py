class Producto:
    __numeroSerie=0
    __tipo=''
    __marca=''
    __problema=''
    __observaciones=''

    def __init__(self,numeroSerie=0,tipo='',marca='',problemas='',observaciones=''):
        assert isinstance(numeroSerie,int)
        assert isinstance(tipo,str)
        assert isinstance(marca,str)
        assert isinstance(problemas,str)
        assert isinstance(observaciones,str)
        self.__numeroSerie=numeroSerie
        self.__tipo=tipo
        self.__marca=marca
        self.__problemas=problemas
        self.__observaciones=observaciones

    def getNumeroSerie(self):
        return self.__numeroSerie