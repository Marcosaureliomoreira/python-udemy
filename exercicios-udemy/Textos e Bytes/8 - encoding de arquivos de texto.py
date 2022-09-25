# Encoding e Arquivos de Texto

# Escrevendo o arquivo com o formato utf8 e lendo em latin1, propositalmente para dar erro

# escrevendo arquivos:
with open('pele.txt', 'w', encoding='utf8') as f:
    f.write('pelé')

# lendo arquivos:
with open('pele.txt', 'r', encoding='latin1') as f:
    print(f.read())

