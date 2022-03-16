class Capitulo:
    __titulo=''
    __cantidadPaginas=0

    def __init__(self,titulo='',cantidadPaginas=0):
        assert isinstance(titulo,str)
        assert isinstance(cantidadPaginas,int)
        self.__titulo=titulo
        self.__cantidadPaginas=cantidadPaginas

    def getTitulo(self):
        return self.__titulo

    def getCantidadPaginas(self):
        return self.__cantidadPaginas

    def __str__(self):
        return f'''Título: {self.__titulo}.
Cantidad de páginas: {self.__cantidadPaginas}.
'''