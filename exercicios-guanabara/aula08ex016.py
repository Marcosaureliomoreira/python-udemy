'''from math import trunc
num = float(input('Digite un numero:'))
print('O valor Digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))'''

from math import trunc
peso = float(input('Digite o seu peso normal que irei mostrar o número inteiro kg: '))
print('O valor digitado foi {} e o seu real valor é {}'.format(peso, trunc(peso)))
if peso == 80:
    print('peso normal!')
elif peso < 50:
    print('Abaixo do peso!')
elif 90 < peso <= 100:
    print('Cuidado!')
elif 100 < peso <= 120:
    print('Cuidado, você esta correndo perigo!')
else:
    print('Você esta praticamente morto. Emcomende o CAIXÃO!')




