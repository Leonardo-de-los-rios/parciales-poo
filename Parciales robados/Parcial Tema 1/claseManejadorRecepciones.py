import csv

from claseProducto import Producto

from claseRecepcion import Recepcion

class ManejadorRecepciones:
    __recepciones=[]

    def __init__(self):
        self.__recepciones=[]

    def addRecepcion(self,unaRecepcion):
        assert isinstance(unaRecepcion,Recepcion)
        self.__recepciones.append(unaRecepcion)

    def leerArchivo(self):
        archivo=open('recepcion2.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        i=0
        for fila in reader:
            if bandera:
                bandera=False
            else:
                idReparacion=int(fila[0])
                fechaRecepcion=fila[1]
                tipo=fila[2]
                marca=fila[3]
                problema=fila[4]
                observaciones=fila[5]
                unProducto=Producto(i,tipo,marca,problema,observaciones)
                unaRecepcion=Recepcion(idReparacion,fechaRecepcion,unProducto)
                self.addRecepcion(unaRecepcion)
                i+=1