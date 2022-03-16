from claseAparatoTec import AparatoTec

class Televisor(AparatoTec):
	__tipoPantalla=''
	__pulgadas=0.0
	__tipoDef=''
	__conexInternet=False
	
	def __init__(self,marca='',modelo='',color='',paisFab='',precioBase=0.0,tipoPantalla='',pulgadas=0.0,tipoDef='',conexInternet=False):
		assert isinstance(tipoPantalla,str)
		assert isinstance(pulgadas,float)
		assert isinstance(tipoDef,str)
		assert isinstance(conexInternet,bool)#revisar
		super().__init__(marca,modelo,color,paisFab,precioBase)
		self.__tipoPantalla=tipoPantalla
		self.__pulgadas=pulgadas
		self.__tipoDef=tipoDef
		self.__conexInternet=conexInternet
		
	def porcentaje(self):
		porcentaje=0.0
		if self.__tipoPantalla=='SD':
			porcentaje+=self.getPrecioBase()*0.01
		elif self.__tipoPantalla=='HD':
			porcentaje+=self.getPrecioBase()*0.02
		elif self.__tipoPantalla=='FULL HD':
			porcentaje+=self.getPrecioBase()*0.03
		elif self.__conexInternet == True:
			porcentaje+=self.getPrecioBase()*0.1
		return porcentaje
		

	'''def calculaImporte(self):
		importe=self.getPrecioBase()
		if self.__tipoPantalla=='SD':
			importe+=importe*0.01
		elif self.__tipoPantalla=='HD':
			importe+=importe*0.02
		elif self.__tipoPantalla=='FULL HD':
			importe+=importe*0.03
		elif self.__conexInternet == True:
			importe+=importe*0.1
		return importe'''