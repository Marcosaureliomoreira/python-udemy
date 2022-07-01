#Crie uma tupla com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,na ordem da colocação. Depos mostre:
# A)Apenas os 5 primeiros colocados.
# B)Os últimos 4 colocados da tabela.
# C)Uma lista com os times em ordem alfabética.
# d)Em que posição da tabela está o time da chapecoense.

#Desafio extra:Perguntar ao usuário se ele quer continuar com o programa.

'''print('-' *150)
print('Lista de Times: Atlético-MG, Flamengo, Palmeiras, Corinthians, Bragantino, Fortaleze, Fluminense, Améria-MG, Ceará, Internacional, Santos, São Paulo, Atlético Goianiense, Juventude, Cuiabá, Atlético PR, Bahia, Grêmio, Sport, Chapecoense')
print('-' * 150),
tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Bragantino', 'Fortaleze', 'Fluminense', 'Améria-MG', 'Ceará', 'Internacional', 'Santos', 'São Paulo', 'Atlético Goianiense', 'Juventude', 'Cuiabá', 'Atlético PR', 'Bahia', 'Grêmio', 'Sport', 'Chapecoense')
print('Os 5 primeiros colocados do brasileirão são: ')
print(tabela[0:5])
print('-=-' * 45)
print('Os 4 últimos colocados do brasileirão são: ')
print(tabela[16:])
print('-=-' * 45)
print('A tabela do Brasileirão em ordem alfabética é: ')
print(sorted(tabela))
print('-=-' * 45)
print(f'A posição em que se encontra a equipe da chapecoense no Brasileirão é:{tabela.index("Chapecoense")+1} posição')'''




num = int(input('Digite um número para iniciar: '))

while True:

    print('-' *150)
    print('Lista de Times: Atlético-MG, Flamengo, Palmeiras, Corinthians, Bragantino, Fortaleze, Fluminense, Améria-MG, Ceará, Internacional, Santos, São Paulo, Atlético Goianiense, Juventude, Cuiabá, Atlético PR, Bahia, Grêmio, Sport, Chapecoense')
    print('-' * 150)
    tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Bragantino', 'Fortaleze', 'Fluminense', 'Améria-MG', 'Ceará', 'Internacional', 'Santos', 'São Paulo', 'Atlético Goianiense', 'Juventude', 'Cuiabá', 'Atlético PR', 'Bahia', 'Grêmio', 'Sport', 'Chapecoense')
    print(f'Os 5 primeiros colocados do brasileirão são:{tabela[0:5]}' )
    print('-=-' *40)
    print(f'Os 4 últimos colocados da tabela é:{tabela[15:]}')
    print('-=-' *40)
    print(f'A tabbela do campeobato brasileiro em ordem alfabética é:{sorted(tabela)}')
    print('-=-' *40)
    print(f'A chapecoense está na posição {tabela.index("Chapecoense")+1}')
    opção = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opção == 'N':
        break

'''tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Bragantino', 'Fortaleze', 'Fluminense', 'Améria-MG', 'Ceará', 'Internacional', 'Santos', 'São Paulo', 'Atlético Goianiense', 'Juventude', 'Cuiabá', 'Atlético PR', 'Bahia', 'Grêmio', 'Sport', 'Chapecoense')
print(f'O time do Flamengo esta na posição {tabela.index("Flamengo")}.')
print('-' *35)
print(f'A tabela do Campeonato em ordem alfabética é: {sorted(tabela)}')'''









