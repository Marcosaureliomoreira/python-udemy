import math

'''angulo = float(input('Digite o angulo que você deseja:'))
seno = math.sin(math.radians(angulo))
print('O angulo de {} teo o seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos (math.radians(angulo))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))'''

from math import radians
angulo = float(input('Digite o angulo: '))
seno = math.sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(radians(angulo))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))