from re import A


class Sabor:
    __numero=0
    __nombre=''
    __descripcion=''

    def __init__(self,numero=0,nombre='',descripcion=''):
        assert isinstance(numero,int)
        assert isinstance(descripcion,str)
        assert isinstance(descripcion,str)
        self.__numero=numero
        self.__nombre=nombre
        self.__descripcion=descripcion
    
    def getNombre(self):
        return self.__nombre