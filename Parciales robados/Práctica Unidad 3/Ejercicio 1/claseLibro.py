from claseCapitulo import Capitulo

class Libro:
    __idLibro=0
    __titulo=''
    __autor=''
    __editorial=''
    __isbn=0
    __cantidadCapitulos=0
    __capitulos=[]

    def __init__(self,idLibro=0,titulo='',autor='',editorial='',isbn=0,cantidadCapitulos=0):
        assert isinstance(idLibro,int)
        assert isinstance(titulo,str)
        assert isinstance(autor,str)
        assert isinstance(editorial,str)
        assert isinstance(isbn,int)
        assert isinstance(cantidadCapitulos,int)
        self.__idLibro=idLibro
        self.__titulo=titulo
        self.__autor=autor
        self.__editorial=editorial
        self.__isbn=isbn
        self.__cantidadCapitulos=cantidadCapitulos
        self.__capitulos=[]
    
    def crearCapitulo(self,titulo,cantidadPaginas):
        assert isinstance(titulo,str)
        assert isinstance(cantidadPaginas,int)
        unCapitulo=Capitulo(titulo,cantidadPaginas)
        self.__capitulos.append(unCapitulo)

    def getId(self):
        return self.__idLibro

    def getTitulo(self):
        return self.__titulo

    def getCapitulos(self):
        return self.__capitulos

    def getAutor(self):
        return self.__autor

    def __del__(self):
        del self.__capitulos

    def __str__(self):
        s=f'''Libro: {self.__titulo}
ID: {self.__idLibro}.
Autor: {self.__autor}.
Editorial: {self.__editorial}.
ISBN: {self.__isbn}.
Cantidad de Capítulos: {self.__cantidadCapitulos}.
'''
        for unCapitulo in self.__capitulos:
            s+=unCapitulo.__str__()+'\n'
        return s