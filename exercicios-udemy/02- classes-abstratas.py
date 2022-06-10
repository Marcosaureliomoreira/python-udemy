#Classe Abstrata
#-Não pode ser instanciada
#-É passada como herança
#-Se possui métodos abstratos, estes devem ser implementados nas classes descendentes
#-Pode conter ou não métodos abstratos

#Métododos Abstratos: São métodos que precisam ser implementados nas classes descendentes

'''class Abstrata:
    def metodo_abstrato(self):
        pass

    def metodo_nao_abstrato(self):
        pass

    class Descendente(Abstrata):
        def __init__(self, nome):
            self.nome = nome


abstrata = Abstrata()

desc = Descendentes('descendentes')'''

from abc import ABC, abstractmethod

class Abstrata(ABC):

    @abstractmethod
    def metodo_abstrato(self):
        pass

    def metodo_nao_abstrato(self):
        pass

class Descendente(Abstrata):
    def __init__(self, nome):
        self.nome = nome

    def metodo_abstrato(self):
        print('Método abstrato implementado')



abstrata = Abstrata()

desc = Descendente('descendente')

desc.metodo_abstrato()