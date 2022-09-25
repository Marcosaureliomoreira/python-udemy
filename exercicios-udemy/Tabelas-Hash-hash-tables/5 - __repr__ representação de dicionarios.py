# get

TAM = 10
# A variável abaixo é nada mais, nada menos que uma lista contendo varias listas vazias, essas listas vázias são chamadas de "slots",
# são lugares vazios prontos para receberem valores. é possível que possa ter mais de um elemento no mesmo slot
hashmaps = [[]for _ in range(TAM)]
#print(hashmaps)

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

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

                                                    # Slots

chave = 'marcos'
valor = 'gokruh'
pos = hash_pos(chave)
chave_existe = False
slot = hashmaps[pos]
# Percorrendo o slot e desempacotando a chave:
for i, cv in enumerate(slot): # [0 (c, v),1 (c,v),2 (c,v)]
    c, v = cv # desempacotando tupla c,v = (c,v)
    if chave_existe == c:
        chave_existe = True
        break
if chave_existe:
    slot[i] = ((chave, valor))
else:
    slot.append((chave, valor))

# mostrando o item dentro do slot:
#print(slot)
# mostrando os slots variando os itens dentro dos slots:
#print(hashmaps)
# mostrando a posição em que esta o item:
#print(pos)

# -----------------------------------------------------------------------------------------------------------------------------

                                            # Função get()


def get(chave, default=None):
    pos = hash_pos(chave)
    slot = hashmaps[pos]
    for cv in slot:
        c, v = cv
        if chave == c:
            return v
    return default


#print(get('marcos'))

# ___________________________________________________________________________________________________________________________________________

# Representação __repr__
# mostrando na prática como um dicionário funciona:

rp = ''
for slot in hashmaps:
    for cv in slot:
        c, v = cv
        if type(c) == str:
            c = f"'{c}'"
        if type(v) == str:
            v = f"'{v}'"
        rp += f'{c}: {v}, '


#print(rp)
# removendo o espaço e a virgula que tem no final:
print('{' + rp[:-2] + '}')
