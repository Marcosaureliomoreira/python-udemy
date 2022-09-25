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
#print('{' + rp[:-2] + '}')

# ___________________________________________________________________________________________________________________________________

                                # Tabela hash completa
# criando o nosso próprio dicionario utilizando classe:

class Hashtable:
    def __init__(self):
        self.TAM = 10
        self.hashmap = [[] for _ in range(self.TAM)]

    def __repr__(self):
        rp = ''
        for slot in self.hashmap:
            for cv in slot:
                c, v = cv
                if type(c) == str:
                    c = f"'{c}'"
                if type(v) == str:
                    v = f"'{v}'"

                rp += f'{c}: {v}, '
        if not rp:
            return '{}'
        return '{' + rp[:-2] + '}'

    def hash_pos(self, chave):
        pos = hash(chave) % self.TAM  # varia entre 0 e (TAM-1)
        return pos

    def define(self, chave, valor):
        pos = self.hash_pos(chave)
        chave_existe = False
        slot = self.hashmap[pos]
        # Percorrendo o slot e desempacotando a chave:
        for i, cv in enumerate(slot):  # [0 (c, v),1 (c,v),2 (c,v)]
            c, v = cv  # desempacotando tupla c,v = (c,v)
            if chave_existe == c:
                chave_existe = True
                break
        if chave_existe:
            slot[i] = ((chave, valor))
        else:
            slot.append((chave, valor))

    def get(self, chave, default=None):
        pos = self.hash_pos(chave)
        slot = self.hashmap[pos]
        for cv in slot:
            c, v = cv
            if chave == c:
                return v
        return default

    # método para adicionar valores a um dicionário:
    # exemplo: h['exemplo'] = 'valor'
    def __setitem__(self, chave, valor):
        return self.define(chave, valor)

    def __getitem__(self, chave):
        return self.get(chave)

    def __len__(self):
        qtd = 0
        for slot in self.hashmap:
            qtd += len(slot)
        return qtd


h = Hashtable()
# adicionando valores derivado do método __getitem__:
h['chave'] = 'valor'
# adicionando novos valores ao dicionário:
h.define('Dois', 2)
h.define('Quatro', 4)
h.define('Cinco', 5)
# Pegando determinado valor no dentro do dicionário usando o método get()
#print(h.get('Dois'))
print(h)
# Verificando a quantidade de itens:
print(len(h))
# Verificando o tipo:
print(type(h))
