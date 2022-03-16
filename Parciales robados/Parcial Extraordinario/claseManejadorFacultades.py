import csv

from claseFacultad import Facultad

class ManejadorFacultades:
    __facultades=[]

    def __init__(self):
        self.__facultades=[]

    def addFacultad(self,unaFacultad):
        assert isinstance(unaFacultad,Facultad)
        self.__facultades.append(unaFacultad)

    def leerArchivo(self):
        archivo=open('Facultades.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                codigo=int(fila[0])
                nombre=fila[1]
                direccion=fila[2]
                localidad=fila[3]
                telefono=fila[4]
                unaFacultad=Facultad(codigo,nombre,direccion,localidad,telefono)
                self.addFacultad(unaFacultad)
        archivo.close()

    def getFacultades(self):
        return self.__facultades

    def __str__(self):
        s=''
        for unaFacultad in self.__facultades:
            s+=unaFacultad.__str__()+'\n'
        return s