#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador de futebol
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida. No final tudo isso será
# guardado em um dicionário, incluindo o total de gols feito durante o campeonato.
'''jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador? '))
tot = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou: '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)'''



'''jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols ele fez na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
print('=' *30)
for k, v, in jogador.items():
    print(f'{k}: {v}')
print('=' *30)
print(f'O Jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')'''


jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols ele fez na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
for k, v, in jogador.items():
    print(f'{k}: {v}')
print('-' * 30)
for i, v, in enumerate(jogador['gols']):
    print(f'Na partida {i+1} foi {v} gols')
print(f'Foi um total de {jogador["total"]} gols')


