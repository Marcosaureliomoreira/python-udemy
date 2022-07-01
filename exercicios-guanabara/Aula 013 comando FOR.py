#AULA 013 Estrutura de repetição FOR
'''for c in range(1, 6):
    print('oi')
print('FIM')'''

'''n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')'''

'''i = int(input('Inicio:'))
f = int(input('fim:'))
p = int(input('passo'))
for c in range(i , f+1, p):
    print(c)
print('FIM')'''

'''for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('fim')'''

s = 0 # SOMANDO VALORES
for c in range(0, 4):
    n = int(input('Digite um valor:'))
    s = s + n
print('O somatório de rodos os valores foi {}'.format(s))