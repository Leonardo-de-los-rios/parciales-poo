from claseManejadorSabores import ManejadorSabores

class Helado:
    __gramos=0
    __sabores=None

    def __init__(self,gramos=0):
        assert isinstance(gramos,int)
        self.__gramos=gramos
        self.__sabores=ManejadorSabores

    def __str__(self):
        s=f'Gramos: {self.__gramos}. Sanores: '
        for unSabor in self.__sabores:
            s+=unSabor.getNombre()+'\n'
        return s