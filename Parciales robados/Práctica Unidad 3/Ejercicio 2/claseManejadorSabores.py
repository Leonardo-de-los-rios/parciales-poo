import csv

from claseSabor import Sabor

class ManejadorSabores:
    __sabores=[]

    def __init__(self):
        self.__sabores=[]

    def addSabor(self,unSabor):
        assert isinstance(unSabor,Sabor)
        self.__sabores.append(unSabor)

    def leerArchivo(self):
        archivo=open('sabores.csv')
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            numero=int(fila[0])
            nombre=fila[1]
            descripcion=fila[2]
            unSabor=Sabor(numero,nombre,descripcion)
            self.addSabor(unSabor)
        archivo.close()

    def getSabores(self):
        return self.__sabores

    def __str__(self):
        s=''
        i=1
        for unSabor in self.__sabores:
            s+=f'{i}. '+unSabor.getNombre() + '\n'
        return s