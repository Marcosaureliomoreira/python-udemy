#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuiir(), dobro() e metade().
#Faça também um programa que importe esse módulo e use algumas funções.


def metade(preço):
    res = preço / 2
    return res


def dobro(preço):
    res = preço * 2
    return res


def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    return res


def diminur(preço, taxa):
    res = preço - (preço * taxa/100)
    return res






