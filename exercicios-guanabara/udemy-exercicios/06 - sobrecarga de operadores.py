
class Numero:
    def __init__(self, num):
        self.num = num

    def __add__(self, outro):
        return int(str(self.num) + str(outro.num))    #Sobrecarregando operadores

    def __repr__(self):
        return f'{self.num}'

    def __eq__(self, other):
        return self.num == other.num

#Caso queira uma concatenar dois números basta mudar para str adicionando aspas para transformar em string

n1 = Numero(2)
n2 = Numero(2)
n3 = n1 + n2

print(n1 + n2)
print(n3 - 15)
print(n1)
print(n2)
print(n1 == n2)
# para mostrar os tipos de operadores: print(dir(n1))