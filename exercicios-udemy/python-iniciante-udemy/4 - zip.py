
# Função zip()

'''l1 = 'banana batata couve frango'.split()
print(l1)
l2 = 'fruta legume verdura carne'.split()
print(l2)

# O zip() vai unir as duas listas acima.

lista_zipada = zip(l1, l2)
# abaixo teremos uma lista com tuplas concatenados
print(list(lista_zipada))'''

#-----------------------------------------------------------------------------------------------------------------------

# Adicionando números(index) no final no começo dos campos:

indexes = range(4)
campos = 'nome idade sexo cidade'.split()
dados = 'pedro 39 homem santos'.split()

print(list(zip(indexes, campos, dados)))

# Usando zip acompanhado do for:

for idx, campo, dado in zip(indexes, campos, dados):
    print(f'{idx}| {campo}: {dado}')
