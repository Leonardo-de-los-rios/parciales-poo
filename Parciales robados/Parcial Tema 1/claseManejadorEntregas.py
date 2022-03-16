import csv

from claseEntrega import Entrega

class ManejadorEntregas:
    __entregas=[]

    def __init__(self):
        self.__entregas=[]

    def addEntrega(self,unaEntrega):
        assert isinstance(unaEntrega,Entrega)
        self.__entregas.append(unaEntrega)

    def leerArchivo(self):
        archivo=open('entregas.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            