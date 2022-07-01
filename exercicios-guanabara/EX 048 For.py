#Ex 048
'''Faça um programa qua calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
s = 0
cont = 0
for c in range(1, 501, 2):
    if (c % 3) == 0:
        s = s + c        # S += c
        cont = cont + 1  # cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, s))


print('FIM')