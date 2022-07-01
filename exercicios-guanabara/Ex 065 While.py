#Ex 065
#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e
#qual foi o maior e o menor valores lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''r = 'S'
soma = 0
media = 0
quant = 0
maior = 1
menor = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    r = str(input('Deseja continuar? []S/N')).upper().strip()[0]
    soma = soma + n
    media = soma / quant
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('O maior número digitado foi:{} e o menor número digitado foi:{}'.format(maior, menor))
print('Foram digitados {} e sua media é de {:.2f}.'.format(quant, media))'''

r = 'S'
soma = 0
quant = 0
media = 0
maior = 1
menor = 0
while r in 'Ss':
    num = int(input('Digite um número: '))
    r = str(input('Deseja continuar?')).upper().strip()[0]
    soma += num
    quant += 1
    media = soma / quant
    if quant == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num


print('O maior número digitado foi:{} e o maior número digitado foi:{}'.format(maior, menor))
print('Foram digitados {} números e a média entre eles é:{:.2f}'.format(quant, media))



