"""
v1 = vetor(2,4)
v2 = vetor(2,1)
v1 + v2 = vetor(4,5)

v = Vetor(3,4)
abs(v)

5

"""

from math import hypot

class Vetor:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    # "repr" significa representação. como vai ficar a saída do código.
    def __repr__(self):
        return f'Vetor({self.x}, {self.y})'

    # retornando a hipotenusa.
    # "abs" de absoluto, retornando o valor absoluto.
    def __abs__(self):
        return hypot(self.x, self.y)

    # "bool" False ou True
    def __bool__(self):
        return bool(self.x or self.y)

    # "add" método para adição
    def __add__(self, outro):
        x = self.x + outro.x
        y = self.y + outro.y
        return Vetor(x, y)

    # "mul" método para multiplicação
    def __mul__(self, escalar):
        return Vetor(self.x * escalar, self.y * escalar)


# instanciando a classe:
v1 = Vetor(2, 4)
v2 = Vetor(2, 1)

# mostrando a soma na tela
print(v1 + v2)

#mostrando na tela os valores booleanos:
print(bool(v1))
print(bool(v2))

# especificando um valor para boolean e mostrando na tela.
print(bool(0))

# retornando o valor absoluto "abs".
v = Vetor(3, 4)
print(abs(v))

# multiplicando v1 que vale: (2,4). irá retornar (4,8).
print(v1 * 2)

# multiplicando v2 que vale: (2,1) por 3. irá retornar: (2,1).
print(v2 * 3)

