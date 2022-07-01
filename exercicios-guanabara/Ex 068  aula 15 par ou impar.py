#Ex 068
#Faça um programa que jogue par ou impar com o computador. ) jogo só será interrompido quando o jogador perder. mostrando o
#total de vitórias consecutivas que ele conquistou no final do jogo.
'''from random import randint
v = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [PI] ')).strip().upper()[0]
    print(f'VocÊ jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print(' DEU PAR' if total %2 == 0 else ' DEU ÌMPAR')
    if tipo == 'p':
        if total %2 == 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('VocÊ PERDEU!')
            break
    elif tipo == 'I':
            if total %2 == 1:
                print('você VENCEU!')
                v += 1
            else:
                print('você PERDEU!')
                break
    print('Vamos jogar novamente...')'''


'''from random import randint
v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(1, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str('Ímpar ou Par? [P/I] ').strip().upper()[0]
        print(f'Você jogou {jogador} e o computador jogou {computador} e o total foi {total}', end= '')
        print('DEU PAR' if total %2 == 0 else 'DEU ÌMPAR')
        if tipo == 'P':
            if total %2 == 0:
                print('Você Venceu!')
                v += 1
            else:
                print('Você Perdeu!')
                break
        elif tipo == 'I':
            if total %2 == 1:
                print('VocÊ Venceu!')
                v += 1
            else:
                print('Você Perdeu!')
                break
    print('Vamos Jogar novamente...')'''


from random import  randint






















