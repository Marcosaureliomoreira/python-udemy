preço = float(input('Digite o preço do produto: '))
novo = preço - preço * 5 / 100

print('O preço do produto custava R${:.2f} com o desconto de 5% fica em R${:.2f}'.format(preço, novo))