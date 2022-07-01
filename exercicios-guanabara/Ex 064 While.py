#Ex 064
#Crie um programa que leia vários números inteiros pelo taclado. O computador só vai parar quando o usuário digitar 999,
#que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderandoo flag.)
'''n = 0
cont = 1
soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n < 999:
        cont += 1
        soma += n
print('Foram digitados {} números e a soma entre eles é:{}'.format(cont, soma))'''

'''n = 0
cont = 0         #n = cont = soma = 0    Atribuição de variáveis, posso fazer todos na mesma linha, pq todos recebem 0.
soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
        cont += 1
        soma += n
        n = int(input('Digite um número [999 para parar]: '))
print('Foram digitados {} números e a soma desses números é:{}'.format(cont, soma))'''
num = quant = soma = 0
num = int(input('Digite um número: '))
while num != 999:
        quant += 1
        soma += num
        num = int(input('Digite um número: '))
print('Foram digitados {} números e a soma entre eles é {}'.format(quant, soma))