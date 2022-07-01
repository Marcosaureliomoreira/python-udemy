#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
#a expressão passada está com os parênteses abertos e fechado na ordem correta.
#Exemplo de expressão correta. ((A+b) * c)
#Exemplo de expressã incorreta. ((a+b)*(a*c)-2

'''expre = str(input('Digite a expressão: '))
pilha = []
for simb in expre:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')'''


'''pilha = []
expre = str(input('Digite a sua expressão: '))
for simb in expre:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta válida!')
else:
    print('Sua expressão esta inválida!')
#((a+b)* c)'''

'''expre = str(input('Digite a sua expressão: '))
lista = []
for simbolo in expre:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está inválida!')'''



expres = str(input('Digite sua expressão: '))
lista =[]
for simb in expres:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Sua lista está válida')
else:
    print('Sua lista está inválida!')




