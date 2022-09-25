TAM = 10
# A variável abaixo é nada mais, nada menos que uma lista contendo varias listas vazias, essas listas vázias são chamadas de "slots",
# são lugares vazios prontos para receberem valores. é possível que possa ter mais de um elemento no mesmo slot
hashmaps = [[]for _ in range(TAM)]
print(hashmaps)




# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Função hash:
# É o ato de mascararmos alguma coisa:

# O comando abaixo "hash" vai mostrar uma cháve(código) para determinado(a) palavra, frase números(entre aspas). isso inclui espaços.
# toda vez que digitarmos a mesma palavra, será a mesma chave(código) para ela.
# Obs: O hash do número inteiro é o próprio número inteiro

# print(hash('Marcos'))

'''O último número que sobrar é o resultado do percent(resto da divisão) pela quantidade de hashs Exemplo: 10 % 5'''

# % é o resto da divisão:
#print(17 % 10) # quanto que sobra
# Resultado: 7

#print(-36 % 10) # quanto que falta
# Resultado: 4

#print(36 % 10)

#print(30 % 10)

# função que vai gerar posição:
def hash_pos(chave):
    pos = hash(chave) % TAM # varia entre 0 e (TAM-1)
    return pos


print(hash_pos('d'))
