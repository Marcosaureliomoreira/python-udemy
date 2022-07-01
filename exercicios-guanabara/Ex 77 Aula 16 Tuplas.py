#Crie um programa que tenha uma tupla com varias palavras (não usar acentos). Depois disso, você deverá mostrar,
#para cada palavra, quais são as vogais.

palavras = ('cao',
            'gato',
            'barata',
            'elefante',
            'leao',
            'peixe',
            'gorila',
            'tigre',
            'tubarao')
'''for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')'''






for a in palavras:
    print(f'\nNa palavra {a} temos as vogais: ', end='')
    for l in a:
        if l in 'aeiou':
            print(f'{l} ', end='')
