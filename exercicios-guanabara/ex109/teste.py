
from ex109 import moeda


p = float(input('Digite o preço: R$ '))
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'Aumentando em 10 % é {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo em 13% temos {moeda.aumentar(p, 13, True)}')
