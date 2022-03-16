from claseCarrera import Carrera

class Facultad:
    __codigo=0
    __nombre=''
    __direccion=''
    __localidad=''
    __telefono=''
    __carreras=[]
    
    def __init__(self,codigo=0,nombre='',direccion='',localidad='',telefono=''):
        assert isinstance(codigo,int)
        assert isinstance(nombre,str)
        assert isinstance(direccion,str)
        assert isinstance(localidad,str)
        assert isinstance(telefono,str)
        self.__codigo=codigo
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono
        self.__carreras=[]
    
    def crearCarrera(self,codigo,nombre,fechaInicio,duracion,titulo):
        unaCarrera=Carrera(codigo,nombre,fechaInicio,duracion,titulo)
        self.__carreras.append(unaCarrera)

    def getCodigo(self):
        return self.__codigo

    def __str__(self):
        s= f'''Código: {self.__codigo}.
Nombre: {self.__nombre}.
Dirección: {self.__direccion}.
Localidad: {self.__localidad}.
Teléfono: {self.__telefono}.
Carreras:'''
        for unaCarrera in self.__carreras:
            s+='\t'+unaCarrera.__str__()+'\n'
        return s