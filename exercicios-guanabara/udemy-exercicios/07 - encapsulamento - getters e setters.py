class Computador:
    def __init__(self, cor, hd):
        self.__cor= cor
        self.__hd = hd

    def get_cor(self):               #Acessando atributos privados com o método "get".
        return self.__cor

    def set_cor(self, valor):        #Atualizando a cor com o método "set".
        self.__cor = valor

pc1 = Computador('branco', 500)
print(pc1.get_cor())

pc1.set_cor('Amarelo')
print(pc1.get_cor())
#=====================================================================================================================
class Fixa:
    def __init__(self):
        self.publico = 'publico'
        self._privado_por_convencao = 'privado por convenção'
        self.__privado_mesmo = 'privado mesmo'

    def get_publico(self):
        return self.publico

    def set_publico(self, valor):
        self.publico = valor

    def get_privado_por_convencao(self):
        return self._privado_por_convencao

    def get_privado_mesmo(self):
        return self.__privado_mesmo


'''fixa = Fixa()
print(fixa.publico)

print(fixa._privado_por_convencao)

fixa._privado_por_convencao = 'Modificando atributo modificado por convenção'
print(fixa._privado_por_convencao)
print(fixa.__privado_mesmo)'''