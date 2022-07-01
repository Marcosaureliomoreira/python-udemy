#Aula 15 Interrompendo repetições while.
'''while True:
    print(cont, '', end='') #executará o programa que está dentro do While True de for infinita.
    cont += 1
print('Acabou')'''

'''n = s = 0
while True:
    n = int(input('Digite um número: '))  #Comando break interrompe o while.
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma desses vale {s}')    # Outra maneira de se escrever, na mais recente atualização do python.'''

#Outros exemplos com a nova F STRINGS.
print('-=' * 60)
nome = 'José'
idade = 33
salário = 987.3
print(f'O {nome} tem {33} anos e ganha {salário:.2f}')



