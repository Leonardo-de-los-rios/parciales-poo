import csv

from claseLibro import Libro

class ManejaLibros:
    __libros=[]

    def __init__(self):
        self.__libros=[]
    
    def addLibro(self,unLibro):
        assert isinstance(unLibro,Libro)
        self.__libros.append(unLibro)

    def leerArchivo(self):
        archivo=open('libros.csv')
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            idLibro=int(fila[0])
            tituloLibro=fila[1]
            autor=fila[2]
            editorial=fila[3]
            isbn=int(fila[4])
            cantidadCapitulos=int(fila[5])
            unLibro=Libro(idLibro,tituloLibro,autor,editorial,isbn,cantidadCapitulos)
            for fila_1 in reader:
                tituloCap=fila_1[0]
                cantidadPaginas=int(fila_1[1])
                unLibro.crearCapitulo(tituloCap,cantidadPaginas)
                cantidadCapitulos-=1
                if cantidadCapitulos==0:
                    break
            self.addLibro(unLibro)
        archivo.close()

    def buscarLibro(self,idLibro):
        se_encontro=False
        i=0
        while se_encontro ==False and i<len(self.__libros):
            if self.__libros[i].getId()==idLibro:
                se_encontro=True
            else:
                i+=1
        if se_encontro:
            print(f'Titulo: {self.__libros[i].getTitulo()}.')
            print('Capítulos:')
            for capitulo in self.__libros[i].getCapitulos():
                print(f'Título: {capitulo.getTitulo()}.')
                print(f'Cantidad de páginas: {capitulo.getCantidadPaginas()}')
        else:
            print(f'No se encontró el Libro con el ID: {idLibro}.')

    def buscarPalabra(self,palabra):
        se_encontro=False
        for unLibro in self.__libros:
            if unLibro.getTitulo().lower().find(palabra.lower()) != -1:
                se_encontro=True
                print(f'Título: {unLibro.getTitulo()}.')
                print(f'Autor: {unLibro.getAutor()}.')
            else:
                i=0
                capitulos=unLibro.getCapitulos()
                while se_encontro==False and i<len(capitulos):
                    if capitulos[i].getTitulo().lower().find(palabra.lower())!=-1:
                        se_encontro=True
                        print(f'Título: {unLibro.getTitulo()}.')
                        print(f'Autor: {unLibro.getAutor()}.')
                    else:
                        i+=1
        if se_encontro == False:
            print(f'No se encontraron libros ni capítulos con la palabra: {palabra}.')


    def __str__(self):
        s=''
        for libro in self.__libros:
            s+=libro.__str__() + '\n'
        return s