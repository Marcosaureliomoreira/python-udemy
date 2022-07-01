                                         #DESAFIO 093
#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador de futebol
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida. No final tudo isso será
# guardado em um dicionário, incluindo o total de gols feito durante o campeonato.

'''jogador = dict()
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
print(f'Foi um total de {jogador["total"]} gols')'''




                                         #DESAFIO 095
#Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detales do aproveitamento
# de cada jogador.

jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' *40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca > len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LENANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'  No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('Volte Sempre!')






