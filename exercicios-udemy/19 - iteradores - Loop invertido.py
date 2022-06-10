#criando uma classe e descobrindo como funciona o for.


class Inverso:
    """Iterador para realizar loops de trás para frente"""
    def __init__(self, dados):
        self.dados = dados
        self.index = len(dados)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.dados[self.index]



inv = Inverso('missa') # Teremos a palavra "missa" invertida.
for elemento in inv:
    print(elemento)
