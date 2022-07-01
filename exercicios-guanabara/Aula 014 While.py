#Aula 014 estrutura de repetição WHILE
'''indentação while

enquanto não maçã:                   while not aple:
    se chão                            if chão:
       passo                              passo
    se buraco                          if buraco:
       pula                               pula
    se moeda                           if moeda:
       pega                               pega
pega                                 pega'''

'''for c in range(1, 10):
    print(c)
print('Fim')        <<<COM FOR'''

'''c = 1
while c < 10:
    print(c)
    c = c +1
print('Fim')        <<<COM WHILE'''

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? []S/N ')).upper()
print('Fim')

'''n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar +=1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))'''