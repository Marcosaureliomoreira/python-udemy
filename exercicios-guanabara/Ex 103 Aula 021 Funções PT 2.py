#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: O nome de um Jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostra a ficha do jogador, Mesmo qua algum dado não tenha sido informado corretamente.


'''def ficha(nome=, gols=):
    return f'O jogador {nome} fez {gols} gols.'''''

'''def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Digite o Nome de um Jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():  #Com este método consigo verificar se o que foi digitado é um número.
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)'''




'''def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols(s) no campeonato.')





n = str(input('Nome do Jogador? '))
g = str(input('Quantidade de gols marcados: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)'''



def ficha(jog='<desconhecido>', gols=0):
    print(f'O {jog} fez {gols} gols(s) no campeonato.')






n = str(input('Nome do jogador: '))
g = str(input('Quantos gols o jogador fez? '))



if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)





























