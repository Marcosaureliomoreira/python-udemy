#GENERATOR EXPRESSIONS - EXPRESSÃO DE GERADORES

dados = 'ralos'
print(list(dados[i] for i in range(len(dados)-1, -1, -1))) # invertendo valor da variável "dados"

print(sum(i * 10 for i in range(10))) # mostrando soma com o "for"

vetor_x = [10, 20, 30]
vetor_y = [7, 5, 3]

# comparando vetores com o método "zip" e somando com o "sum".
# primeiro vai multiplicar valores por valores: 10 * 7, 20 * 5, 30 * 3. e no final vai somar o vetor_x + vetor_y que var dar 260.
print(sum(x * y for x,y in zip(vetor_x, vetor_y)))

