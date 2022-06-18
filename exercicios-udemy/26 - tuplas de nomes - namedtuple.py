from collections import namedtuple

campos = 'nome tamanho cor quantidade'.split()
print(campos)

Roupas = namedtuple('Roupa', 'nome tamanho cor quantidade') # <<< classe.
vestido = Roupas('vestido', 'M', 'azul', 20)

# acessando todos as caracteriticas de vestido:
print(vestido)

# acessando por nome:
print(vestido.tamanho)
print(vestido.quantidade)

# acessando por index:
print(vestido[2])

# acessando os capos da classe:
print(Roupas._fields) # "fields" = campos

# tranformando em dicionário
print(vestido._asdict())

# acessando o dicionário com o método ".itens":
print(vestido._asdict().items())

for campo, valor in vestido._asdict().items():
    print(f'{campo}: {valor} ')
