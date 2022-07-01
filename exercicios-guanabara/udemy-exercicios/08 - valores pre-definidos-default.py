class Retangulo:
    def __init__(self, altura=10, largura=20):
        self.altura = altura
        self.largura = largura
        self.largura = altura

    @property  #propriedade
    def area(self):        # Esta função serve caso atualizamos o valor da altura e largura em algun lugar a abaixo e este método garante que a área será atualizada.
        return self.largura * self.altura



ret1 = Retangulo()
ret2 = Retangulo()

print(ret1.largura)
print(ret1.altura)



ret1.altura = 30
ret2.largura = 5
print(ret1.area)

#======================================================================================================================

class Pessoa:
    def __init__(self, nome, ano_nasc, ano_atual):
        self.nome = nome
        self.idade = ano_atual - ano_nasc

pedrinho = Pessoa('Pedrinho', 1995, 2022)
#print(pedrinho.idade)