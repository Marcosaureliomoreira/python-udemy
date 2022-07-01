'''print(lanche [1:])    <<<mostra o preimeiro elemento até o final.>>>
print(lanche[-1])     <<<mostrano último elemento. se queser mostrar o penúltimo é [-2] e assim por diante>>>

len(lanches) <<<<Vai informar quantos elementos tem a variável lanche.

É possível usar o For em variáveis compostas.

Exemplo: for c in lanche:            <<<<Vai imprimmir os elementos que existem dentro da variável lanche.
            print(c)
'''

# AS TUPLAS SÁO IMUTÁVEIS. <<<não é possível mudar a tupla.
# NO caso de fatiamento o último elemento é sempre ignorado.


'''lanche = ('hamburger', 'suco', 'pizza', 'pudim')
print(lanche[0])'''

'''lanche = ('hamburger', 'suco', 'pizza', 'pudim')
for comida in lanche:
    print(f'Hoje vou comer {comida}')
print('Delícia!!!')'''

'''lanche = ('hamburger', 'suco', 'pizza', 'pudim', 'batata frita')
#print(len(lanche))
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('Comi pra caramba!')'''


'''lanche = ('hambuerger', 'suco', 'pizza', 'pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')     #<<<MANEIRA CLÁSSICA DE SE ESCREVER.
print('QUE DELÍCIA!')'''


lanche = ('hambuerger', 'suco', 'pizza', 'pudim')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')      # <<<MANEIRA DE SE ESCREVER QUUANDO PRECISO DA POSIÇÃO (DADOS) DOS ITENS.

#print(sorted(lanche))            #<<<Comando para organizar uma tupla (ordem alfabética).

#Usar o deslocamento quando existir dois números iguais ba mesma tupla sob o com .index EXEMPLO: print('c.index(5, 1))

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b        #<<<somando uma tupla com a outra.
print(c)
#print(len(c))
#print(c.count(5))            #<<<Mostra quantas vezes aparece o número 5.
print(c.index(5))          # <<<Mostra em que posição está o número 4.'''

'''#Posso ter dados de tipos diferentes de variáveis dentro das minha tuplas. EXEMPLO ABAIXO:
pessoa = ('Gustavo', 39, 'M', 99.88)
#del (pessoa)      <<<Comando para apagar uma tupla inteira... É possível utilizar esse comando para qualquer coisa no python.
print(pessoa)'''

#Sorteando 5 números aleatórios e colocando em uma tupla.
from random import randint
n = (randint(1, 6), randint(1, 6,), randint(1, 6,),
     randint(1, 6,), randint(1, 6, ))
print(f'O número sorteado foi {n} ')