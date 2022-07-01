'''nome = str(input('Qual é seu nome?')).strip()
if nome == 'Marcos':
    print('Olá,que nome lindo vc tem!')
else:
    print('seu nome é bem comum!')
print('Bom dia, {}'.format(nome))'''


'''n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print('A sua media foi:{:.1f}'.format(m))
if m > 6.0:
    print('\033[32mA sua media foi boa! PARABENS!')
else: print('\033[31mA sua media foi ruim! ESTUDE MAIS!')'''


#MAIOR E MENOR NÚMERO:

'''a = int(input('digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

print(f'O maior número foi:{maior}')
print(f'O menor número foi:{menor}')'''
maior = menor =  cont = num = soma = contpar = contimpar = somaimpar = média = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont +=1
    soma += num
    média = soma / cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if num %2 == 0:
        contpar += 1
    elif num %2 == 1:
        contimpar +=1
        somaimpar += num









print(f'Fora digitados {contpar} pares e {contimpar} números ímpares.')
print(f'Foram digitados {cont} números.')
print(f'O maior número foi: {maior}')
print(f'O menor número foi: {menor}')
print(f'A soma de todos os números ímapares é {somaimpar}')
print(f'A soma de todos os números digitados é {soma}')
print(f'A média desse números é {média}.')









