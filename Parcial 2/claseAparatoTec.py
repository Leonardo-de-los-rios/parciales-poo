from abc import ABC
import abc

class AparatoTec(ABC):
	__marca=''
	__modelo=''
	__color=''
	__paisFab=''
	__precioBase=0.0
	__importeVenta=0.0
	
	def __init__(self,marca='',modelo='',color='',paisFab='',precioBase=0.0):
		assert isinstance(marca,str)
		assert isinstance(modelo,str)
		assert isinstance(color,str)
		assert isinstance(paisFab,str)
		assert isinstance(precioBase,float) and precioBase>0
		
		self.__marca=marca
		self.__modelo=modelo
		self.__color=color
		self.__paisFab=paisFab
		self.__precioBase=precioBase
		self.__importeVenta=0.0
		
	'''@abc.abstractmethod
	def calculaImporte():
		pass
		
	def setImporte(self,importe):
		assert isintance(importe,float) and importe>0
		self.__importeVenta=importe'''
		
	@abc.abstractmethod
	def porcentaje():
		pass
	
	def calculaImporte(self):
		self.__importeVenta=self.__precioBase+self.porcentaje()
	
	def getPrecioBase(self):
		return self.__precioBase
		
	def getMarca(self):
		return self.__marca
		
	def getImporte(self):
		return self.__importeVenta
		
	def getPais(self):
		return self.__paisFab