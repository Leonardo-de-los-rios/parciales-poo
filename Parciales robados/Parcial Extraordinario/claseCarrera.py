class Carrera:
    __codigo=0
    __nombre=''
    __fechaInicio=''
    __duracion=''
    __titulo=''
    
    def __init__(self,codigo=0,nombre='',fechaInicio='',duracion=0,titulo=''):
        assert isinstance(codigo,int)
        assert isinstance(nombre,str)
        assert isinstance(fechaInicio,str)
        assert isinstance(duracion,str)
        assert isinstance(titulo,str)
        self.__codigo=codigo
        self.__nombre=nombre
        self.__fechaInicio=fechaInicio
        self.__duracion=duracion
        self.__titulo=titulo

    def __str__(self):
        return f'''Código: {self.__codigo}.
Nombre: {self.__nombre}.
Fecha de Inicio: {self.__fechaInicio}.
Duración: {self.__duracion}.
Título: {self.__titulo}.
'''