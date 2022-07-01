#LISTAS utilizam colchetes[] ao invés de parentêses() com é o caso das TUPLAS.
#Listas são mitáveis, ou seja podemos mudar um elemento que esta dentro de uma lista. diferentemente de tuplas.EXEMPLO ABAIXO:


'''lanche = ['hamburger', 'suco', 'pizza', 'pudim']    #Subtituindo um elemento em uma lista.
lanche[2] = 'picolé'
print(lanche)'''


lanche = ['hamburger', 'suco', 'pizza', 'pudim']
#lanche.append('biscoito')             #O comando appennd adiciona um novo elemento no final de uma lista como no exmplo ao lado.
#lanche.insert(0,'cachorro quente')    #O comando insert adiciona elementos em qualquer lugar em uma lista. como no exemplo ao lado.
#del lanche[3]                         #O comando del permite excluir um elemento contido em uma lista. como no exemplo ao lado.
#lanche.pop()                          #Este método também permite a exclusão de elementos em uma lista. geralmente é usadon para excluir o último elemento. mas pode ser usado em outras situações.
#lanche.remove('suco')                 #Este comando permite remover um elemento de uma lista usando o nome do elemento. como no exemplo ao lado.
#if 'pizza' in lanche:
    #lanche.remove('pizza')            #Verificar se existe um elemento e elimina conforme o exemplo ao lado.
#valores=list(range(4, 11))            #Declarando listas a partir do método range. IRÁ CRIAR UMA LISTA CHAMADA VALORES COM SEIS ELEMENTOS DENTRO, INICIANDO DE 4 ATÉ 11.
'''valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()                         #O comando sort() ordena os valores de uma lista em ordem crescente. comono exemplo ao lado.
valores.sort(reverse=True)             #O comando sort(reverse=True) ordena os elemetos em ordem reversa ou seja ao contrário. como no exemplo ao lado.
print(len(valores))                     #Verifica quantos elementos há em uma lista. Exeplo ao lado.'''




'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 0)
if 4 in num:
    num.remove(4)
else:
    print('Não encontrei o número 4 na lista.')
print(num)
#print(f'Essa lista tem {len(num)} elementos.')'''

#Outra maneira de mostrar uma lista.
'''valores = list()
valores.append(5)
valores. append(9)
valores.append(4)'''


valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))       #Recebendo números pelo teclado com o método append.
for c, v in enumerate(valores):

    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')

'''a = [2, 3, 4, 7]
b = a[:]                 #<<<Maneira de se fazer uma cópia de lista e poder alterar uma delas sem ter que alterar a outra.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''




















