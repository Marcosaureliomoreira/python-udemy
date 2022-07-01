#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
#999, que a condição de parada. No final, mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag).
num = cont = soma = 0
while num != 999:   #while True:
    num = int(input('Digite um número: (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'foram digitados {cont} números e a soma desses números é {soma}')
