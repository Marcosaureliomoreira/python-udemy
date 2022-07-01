#Adápte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
from ex108 import moeda

p = float(input('Digite o preço: R$ '))
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Aumentando em 10 % é {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo em 13% temos {moeda.moeda(moeda.aumentar(p, 10))}')
