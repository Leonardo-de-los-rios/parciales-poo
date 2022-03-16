from claseHelado import Helado

class ManejadorHelados:
    __helados=[]

    def __init__(self):
        self.__helados=[]

    def addHelado(self,unHelado):
        assert isinstance(unHelado,Helado)
        self.__helaods.append(unHelado)

    def registrarVenta(self,gramos,unManejadorSabores):
        assert isinstance(gramos,int)
        print('Sabores:')
        print(unManejadorSabores)
        sabores=unManejadorSabores.getSabores()
        if gramos == 250:
            sabor=input('Ingrese sabor: ')
            try:
                sabor=int(sabor)
                if 1 <= sabor <= len(sabores):
                    pass
                else:
                    print('Sabor incorrecto.')
            except:
                print('Error')
    
    def __str__(self):
        s=''
        for helado in self.__helados:
            s+=helado.__str__() + '\n'
        return s