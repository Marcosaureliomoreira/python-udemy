#Assistir os exercícios da aula 18 para complementar o aprendizado desta aula.
#listas Parte 2.
'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
print(galera)'''

'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]             #Criando uma cópia da lista.
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]   #Pegando elemenros de uma lista composta.
print(galera[2][0])'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for i in galera:
    #print(i[0])
    print(f'{i[0]} tem {i[1]} anos de idade.')'''

'''galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))       #Criando cópias de listas.
    galera.append(dado[:])
    dado.clear()
print(galera)'''



'''totmai = totmen = 0
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()                          #Recebendo dados, apagando assim que for lido com o comando clear para não repetir 
                                          # a lista e verificando se as pessoas são maiores ou menores de idade.
for p in galera:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print((f'{p[0]} é menor de idade.'))
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')'''




galera = list()
dado = list()
totalmaior = totalmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmenor += 1
print(f'Temos {totalmaior} maiores e {totalmenor} menores de idade.')
