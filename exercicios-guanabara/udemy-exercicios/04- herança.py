#HERANÇA
#Em herança temos:
# SuperCLasse
# SubClasse


'''class poligono:
    __largura = None
    __altura = None

    def set_valores(self, largura, altura):
        self.largura = largura
        self.altura = altura


class retangulo(poligono):
    def get_area(self):
        return self.largura * self.altura


class triangulo(poligono):
    def get_area(self):
        return self.__largura * self.__altura / 2


ret = retangulo()
tri = triangulo()

print(ret.get_area())

#----------------------------------------------------------------------------------------------------------------------
# SUBCLASSES TENDO ACESSO A ATRIBUTOS DE SUPERCLASSE

class poligono:
    __largura = None
    __altura = None

    def set_valores(self, largura, altura):
        self.__largura = largura
        self.__altura = altura

    def get_largura(self):
        return self.__largura

    def set_largura(self, valor):
        self.__largura = valor

    def get_altura(self):
        return self.__altura

    def set_altura(self, valor):
        self.__altura = valor



class retangulo(poligono):
    def get_area(self):
        return self.get_largura() * self.get_altura()


class triangulo(poligono):
    def get_area(self):
        return self.get_largura() * self.get_altura() / 2


tr1 = triangulo()

ret.set_valores(2, 3)
tri.set_valores(5, 2)

print(ret.get_area())
print(tri.get_area())'''






# Herança W3SCHOOLS


class pessoa:
    def __init__(self, pnome, snome):
        self.primeironome = pnome
        self.segundonome = snome

    def imprimirnome(self):
        print(self.primeironome, self.segundonome)


x = pessoa('Marcos', 'Aurélio')
print(x.primeironome, x.segundonome)


# Abaixo a classe estudante está herdando os atributos da classe pai(pessoa), com isso não precisamos colocar a função init.
'''class Estudante(pessoa):
    pass

x = Estudante('Carla', 'Silva')
print(x.primeironome, x.segundonome)'''

#============================================================================================================================

# Quando adicionamos a função __init__ a classe não herdará mais a herança do pai, porém se quisermos herdar temos que fazer
# como no exemplo abaixo:
class Estudante(pessoa):
    def __init__(self, pnome, snome):
        pessoa.__init__(self, pnome, snome)


x = Estudante('José', 'Silva')
print(x.primeironome, x.segundonome)

#=============================================================================================================================

# FUNÇÃO SUPER()

#Python também pode ter uma função super() que fará com que a classe filha herde todos os métodos e propriedades de seu pai.

class Estudante(pessoa):
    def __init__(self, pnome, snome, ano):
        super().__init__(pnome, snome)
        self.graduacao = ano  #Ao lado adicionamos uma variável

x = Estudante('Marcos', 'Aurélio', 2019)
print(x.primeironome, x.segundonome)
print(x.graduacao)



#=======================================================================================================================

class Pai1:
    def __init__(self):
        print('__init__Pa1')


class Pai2:
    def __init__(self):
        print('__init__Pai2')


#Abaixo poderiamos ter usado o método Super para acesar a clas Pai1 e Pai2 como fizemos acima.
class Filho(Pai1, Pai2):
    def __init__(self):
        print('__init__Filho')
        Pai1.__init__(self)
        Pai2.__init__(self)


filho = Filho()
