#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuiir(), dobro() e metade().
#Faça também um programa que importe esse módulo e use algumas funções.


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminur(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='RS'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')





