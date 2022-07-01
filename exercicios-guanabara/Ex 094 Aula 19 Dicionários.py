# Crie um programa que leia nome, sexo, idade de várias pessoas, guardando Os dados de cada pessoa em um dicionário e
# todos os dicionário em uma lista. No final mostre:
#a) Quantas pessoas foram cadastradas.
#b) A media de idade do grupo.
#c) Uma lista com todas as mulheres.
#d) Uma lista com todas as pessoas com idade acima da média.


dados = dict()
lista = list()
contp = soma = media = contm = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Digite o nome: ')).upper().strip()
    dados['idade'] = int(input('Digite a Idade: '))
    dados['sexo'] = str(input('Digite o sexo: ')).upper().strip()[0]
    lista.append(dados.copy())
    contp += 1
    soma += dados['idade']
    media = soma / contp
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print('-' * 30)
print(lista)
print('-' * 30)
print(f' -O total de pessoas cadastradas é {contp} ')
print(f' -A media de idade do grupo é {media:.2f}')
print(' -As Mulheres cadastradas foram ', end='')
for m in lista:
    if m['sexo'] in 'Ff':
        print(f'{m["nome"]} ', end='')
print()
print(f' -As pessoas com idade acima da média são: ', end='')
for p in lista:
    if p['idade'] >= media:
        #print(f'{p["nome"]}', end='')
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<FIM>>')


