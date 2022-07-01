
from ex107 import moeda

p = float(input('Digite o preço: R$ '))
print(f'O dobro de R${p} é RS{moeda.dobro(p)}')
print(f'A metade de RS{p} é RS{moeda.metade(p)}')
print(f'Aumentando em 10 % é RS{moeda.aumentar(p, 10)}')
print(f'Reduzindo em 13% temos RS{moeda.diminur(p, 13)}')
