'''
# Filter ==> similar ao map, ele recebe uma função e uma lista
# o Filter trabalha com boolean(veradeiro ou falso).

numeros = list(range(1, 11))

# retornando números maiores que 5 com a expressão Lambda:
print(list(filter(lambda x: x > 5, numeros)))


# Resultados com compeensão de listas:
# Maneira1
novos_numeros = []
for i in numeros:
    if i > 5:
        novos_numeros.append(i)
print(novos_numeros)

# Maneira2:
print([x for x in numeros if x > 5])
'''
# --------------------------------------------------------------------------------------------------------------------------------------------------------

# Outros exemplos:
# filtrando dados que não sejam vazios:

dados = [0, 'b', 'c', '', '', 'f', '', 'h', 'i', []]

# Com filter:
# retornando uma lista com dados que não sejam vazios, porém esse método não é muito recomendado, caso tenha o número 0, ele será reconhecido como não válido.
print(list(filter(None, dados)))


# Com compreensão de listas:
# retornando uma lista com dados que não sejam vazios
# Maneira 1:

dados_completos = []
for dado in dados:
    if dado != '':
        dados_completos.append(dado)
print(dados_completos)



# Função para retornar verdadeiro ou falso, fazendo um filtro e usando junto com o filter:
#Maneira 2:

def valido(x):
    if x == '':
        return False
    return True


print(list(filter(valido, dados)))


# Fazendo comcompreeensão de listas de outra maneira:
# Maneira 3:

print([x for x in dados if x != ''])




# Função que vai retornar apenas elementos que não forem vázios:
'''def vazio(*lista):
    minha_lista = []
    for item in lista:
        if item != '':
            minha_lista.append(item)
            print(minha_lista)


vazio('a', 3, '', '', 23, 'u', [])'''
