#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
#o usuário quer ou não continuar. No final mostre:
# a) quantas pessoas tem mais de 18 anos.
# b) quantas homems foram cadastrados.
# c) quantas mulheres tem menos de 20 anos.
sexo = ' '
opção = 'S/N'
soma = cont = quantH = quantM = 0
print('-=' * 20)
print('CADASTRO DE PESSOAS')
print('-=' * 20)
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F] ')).upper().strip()[0]
    print('-=' * 20)
    if idade > 18:
        cont += 1
    if sexo == 'M':
        quantH += 1
    if sexo == 'F' and idade < 20:
        quantM += 1
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F] ')).upper().strip()[0]
    opção = str(input('QUER CONTINUAR? [S/N] ')).upper().strip()[0]
    if opção == 'N':
        break
print(f'Total de pessoa com mais de 18 anos é {cont} O total de homens cadastrados é {quantH} E a quantidade de mulheres com menos de 20 anos é {quantM}.')
print('Fim da seção, OBRIGADO E VOLTE SEMPRE!')
