import csv

from claseCarrera import Carrera

from claseManejadorFacultades import ManejadorFacultades

class ManejadorCarreras:
    __carreras=[]

    def __init__(self):
        self.__carreras=[]

    def addCarrera(self,unaCarrera):
        assert isinstance(unaCarrera,Carrera)
        self.__carreras.append(unaCarrera)

    def leerArchivo(self,unManejaFacultades):
        assert isinstance(unManejaFacultades,ManejadorFacultades)
        archivo=open('Carreras.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                codigo=int(fila[0])
                nombre=fila[1]
                titulo=fila[2]
                duracion=fila[3]
                nivel=fila[4]
                codigoFacultad=int(fila[5])
                se_encontro=False
                facultades=unManejaFacultades.getFacultades()
                i=0
                while se_encontro==False and i<len(facultades):
                    if codigoFacultad==facultades[i].getCodigo():
                        unaCarrera=Carrera(codigo,nombre,titulo,duracion,nivel)
                        self.addCarrera(unaCarrera)
                        facultades[i].crearCarrera(codigo,nombre,titulo,duracion,nivel)
                        se_encontro=True
                    else:
                        i+=1
        archivo.close()

    def __str__(self):
        s=''
        for unaCarrera in self.__carreras:
            s+=unaCarrera.__str__()+'\n'
        return s