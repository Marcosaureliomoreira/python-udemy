# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado, Crie uma função input(), mas com a validação
# para aceitar apenas valores monetários.

from ex112.utilidadescev import dado
from ex112.utilidadescev import moeda

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)
