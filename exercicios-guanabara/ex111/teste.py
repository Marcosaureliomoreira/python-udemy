# Crie um pacote chaado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. tranfira todas as funções utili
#zadas nos desafios 107, 108, 109 para o primeiro pacote e mantenha tudp funcionando.
from ex111.utilidadescev import moeda

p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 20, 12)
