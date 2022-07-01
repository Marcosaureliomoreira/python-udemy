'''class carro:
    def __init__(self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo


car1 = carro('prata', 'gm', 'onix')
car2 = carro('branco', 'ford', 'focus')

print(car1.modelo, car1.cor)
print(car2.marca, car2.modelo)


class salario:

    def __init__(self, salario1=100, salario2=200):
        self.salario1 = salario1
        self.salario1 = salario2
        self. resul = salario2 + salario1


sal1 = salario()
sal2 = salario()

print(sal2.resul)'''



                                            # CHAMANDO MÉTODOS DENTRO DE CLASSES

'''class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def minhafunção(self):    # Métodos de objeto
        print('Olá, meu nome é ' + self.nome)

    def saudação(self):
        print('Tudo bem? ' + self.nome)


p1 = pessoa('Marcos', 26)
p1.minhafunção()
p1.saudação()
p2 = pessoa('Jeniffer', 27)
p2.minhafunção()
p2.saudação()
p3 = pessoa('Vitor', 24)
p3.minhafunção()
p3.saudação()'''
#-----------------------------------------------------------------------------------------------------------------------

                                # MODIFICANDO PROPRIEDADES DO OBJETO
                                #   (Modificando o objeto idade)

class pessoa:
    def __init__(self, nome, idade):
        self.mome = nome
        self.idade = idade

    def minhafunção(self):
        print('Olá meu nome é ' + self.mome)

p1 = pessoa('João', 36)
p1.idade = 40

print(p1.idade)

                            #EXCLUINDO UM OBJETO: para excluir basta user "del"
                            #EXEMPLO: del p1.idade: irá excluir a idade.
#-----------------------------------------------------------------------------------------------------------------------


class carro:

    def __init__(self, cor, modelo):
        self.__cor = cor
        self.modelo = modelo

    def get_cor(self):
        return self.__cor


car1 = carro('vermelho', 'polo')
#print(car1.get_cor())




class casa:
    def __init__(self, cor, bairro):
        self.cor = cor
        self.__bairro = bairro

    def minhafunção(self):
        print('A cor da casa é ' + self.cor)

    def get_bairro(self):
        return self.__bairro


house = casa('branca', 'vila nova')
print(house.cor)             #Acessando atributo público
print(house.get_bairro())    #Acessando atributo privado com o método "get"
#=======================================================================================================================

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        if idade >= 18:
            print(f'{self.nome} é Maior de idade')
        else:
            print(f'{self.nome} é Menor de idade')


pessoa = Pessoas('Maria', 20)
pessoa2 = Pessoas('Julia', 10)

#=======================================================================================================================

#Criando classe para clientes Netflix
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        lista_planos = ['basic', 'premium']
        if plano in lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano inválido')

    def imprimir(self):
        return print(f'O {self.nome} Assinou o plano {self.plano}')

cliente = Cliente('Adriano', 'marcos@gmail','basic')
cliente.imprimir()
