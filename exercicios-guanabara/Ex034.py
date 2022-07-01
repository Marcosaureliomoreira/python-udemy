#EXERCÍCIO 34 *PROGRAMA ORIGINAL.
Escreva um programa que pergunte o salário do funcionário e calcule o valor do seu aumento. Para salários
superiores a 1.250,00, calcule um aumento de 10%. para os inferiores ou iguais, o aumento é de 15%.'''

'''salário = float(input('Qual é o salário do funcionário R$?' ))
if salário <= 1250:
    novo = salário + (salário * 15 /100)
else:
    novo = salário + (salário *10 / 100)
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora'.format(salário, novo))

#Crie um programa que leia o preço de um produto e mostre o seu valor de 10% de desconto caso as compras atinjam um valor de R$ 100.00.

'''valor = float(input('Digite o valor das compras:'))
formapag = str(input('Digite a forma de pagamento:'))


if valor >= 100 and formapag==dinheiro:
    desconto = valor - (valor * 10/100)

else:
    print('Compra finalizada!')
    print('O total da sua compra é de R${} com o desconto vai para R${}'.format(valor, formapag, desconto, dinheiro))'''



























