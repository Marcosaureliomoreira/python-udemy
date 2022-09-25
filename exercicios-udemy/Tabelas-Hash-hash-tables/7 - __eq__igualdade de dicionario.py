class Hashtable:
    def __init__(self):
        self.TAM = 10
        self.hashmap = [[] for _ in range(self.TAM)]

    # representação(maneira como será mostrado)
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

    # pegar o item
    def __getitem__(self, chave):
        return self.get(chave)

    # quantidade do item:
    def __len__(self):
        qtd = 0
        for slot in self.hashmap:
            qtd += len(slot)
        return qtd

    # igualdade/equivalência, para comparar elementos:
    def __eq__(self, outro):
        for slot in self.hashmap:
            for cv in slot:
                c, v = cv
                if not outro.get(c):
                    return False
                else:
                    if v != outro.get(c):
                        return False
        return True

h1 = Hashtable()
h2 = Hashtable()
# comparando os dois elementos:
#print(h1 == h2)

h1[10] = 'b'
h1[50] = 'a'

h2[50] = 'a'
h2[10] = 'b'

print(h1)
print(h2)
print(h1 == h2)
