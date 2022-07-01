#Ex 061
#Refaçao o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando termos da progressão usando a estrutura while.
'''print('Geradore de PA')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão da progressão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
'''
'''primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da progressã: '))
print('Gerador de PA')
print('-=' * 12)
termo = primeiro
cont = 1
while cont <= 10:
    print(' {}' .format(termo), end='')
    termo += razão
    cont+=1
print('FIm')'''

primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da progressão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}, ', end=' ')
    termo += razão
    cont += 1








