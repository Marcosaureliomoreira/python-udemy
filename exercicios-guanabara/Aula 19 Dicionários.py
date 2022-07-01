dados = {'nome':'Pedro', 'idade':'25'}
#print(dados)   imprime os elementos que estão dentro de dados.
#print(dados['nome'])   #irá mostrar o nome PEDRO que está dentro de dados.
#print(dados['idade'])  #Irá imprimir a idade 25 que está dentro de dados.
#*** O MÉTODO "APPEND"  NÃO FUNCIONA EM DICIONÁRIOS.
#dados['sexo']='M'      #Adicionando novos elementos.
#del dados['idade']      #Irá remover a idade de dados.
#print(dados)

filme = {'tutulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
        }
#print(filme.values())   #Ira pegar somente a parte de cima do dicionário EXEMPLO: "star wars", "1977", "George Lucas".
#print(filme.keys())     #Irá pegar a parte de baixo do dicionário EXEMPLO: "título", "ano", "diretor".
#print(filme.items())     #Irá podemos usar este elemento para pegar todos os elementos.

#for k,v in filme.items():
    #print(f'O {k} é {v}')  # Podemos usar a estrutura for para listar todos os elementos de dicionário.

#OBS. Não utilizamos o enumerates em dicionários, utilizamos o método "itens".
pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
pessoas['nome'] = 'Marcos'  #Substituindo o nome "Gustavo" pelo nome "Marcos".
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')    #Aqui usamos aspas duplas pq ja estamos dentro de aspas simples.
#for k,v in pessoas.items():
   # print(f'{k} = {v}')





'''brasil = []
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}            #EXEMPLO DE UM DICIONÁRIO DENTRO DE UMA LISTA.
brasil.append(estado1)
brasil.append(estado2)
#print(brasil)
#print(brasil[0])     #Vai mostrar tudo o que está contido em estado1
#print(brasil[1])      #Vai nostrar tudo o que está contido em estado2
#print(brasil[1]['sigla'])  #Vai mostrar a sigla "SP"'''



'''estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())        #É NECESSÁRIO USAR O MÉTODO COPY PARA COPIAR UMA LISTA QUANDO ESTAMOS UTILIZANDO DICIONÁRIOS.
for e in brasil:
    #for k, v in e.items():
        #print(f'O campo {k} tem valor {v}')
    for v in e.values():
        print(v, end=' ')
    print()'''

########################################################################################################################
                                            # OrderedDict(Udêmy)

import collections

d = {'1': 'um', '2': 'dois'}
od = collections.OrderedDict(d) #Para manter a Ordem do dicionário. (irá retornar uma lista de tuplas)
#print(od)
#-----------------------------------------------------------------------------------------------------------------------
c = collections.Counter('Araraquara') #Contará quantas vezes aparece cada letra na frase/palavra
#print(c)

#-----------------------------------------------------------------------------------------------------------------------
#print(c.most_common(3)) # SIGNIFICA: MaisComun: sem parâmetro irá contar todos os números da variável "c". com o
# parâmetro, conta os primeiros elementos de acordo com o número entre parêntese.

#-----------------------------------------------------------------------------------------------------------------------
e = {'1': 'um', '2': 'dois'}
f = {'3': 'três', '4': 'quatro'}

cm = collections.ChainMap(e, f)  # é uma cadeia de mapas, uni os dicionários como se fossem um só.
#print(cm)
#print(cm['3']) #com o ChainMap posso acessar o dicionário normalmente como se fosse um só.
#-----------------------------------------------------------------------------------------------------------------------

                                            # UserDict
# O StrDicttUser vai converter não "strings" para strings"
import collections


class StrDictUsers(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):  # Vai verificar se a chave é uma instância de "str" e se for vamos gerar um erro pq a chave esta faltando e se não for vamos tentar chama-la com str, com o return
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data  # verifica se a chave está em self.data, que é esta contidos no elementos UserDict.

    def __setitem__(self, key, item): # Todas as chaves serão "strings".
        self.data[str(key)] = item    # estamos forçando caso haja uma criação de um novo item no dicionário a ser uma "str", não importa a chave, mesmo assim vai ser "str".


#Agora de qualquer forma que acessarmos o dicionário, será retornado o valor, seja como inteiro ou string.
d = StrDictUsers(d)
d['3'] = 'três'
#print(d['1'])

#=======================================================================================================================

                                        # Dicionário imutável

from types import MappingProxyType
d_prx = MappingProxyType(d) #com essa biblioteca não podemos adicionar novos itens no dicionário.
print(d_prx['2'])







