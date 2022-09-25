# Tabelas Hash

dicionario = {'Chave': 'Valor'}
print(dicionario)
print(type(dicionario))

# Formas de pegar valores com dicionário:
#print(dicionario.get('Chave'))
#print(dicionario['Chave'])

TAM = 10
# A variável abaixo é nada mais, nada menos que uma lista contendo varias listas vazias, essas listas vázias são chamadas de "slots",
# são lugares vazios prontos para receberem valores. é possível que possa ter mais de um elemento no mesmo slot
hashmaps = [[]for _ in range(TAM)]
print(hashmaps)
print(dict())

