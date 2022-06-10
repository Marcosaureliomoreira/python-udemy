"""
PROJETO BARALHO:
"""
import collections

Carta = collections.namedtuple('Carta', ['valor', 'naipe'])
valores = [str(n) for n in range(2, 11)] + (list('JQKA'))
naipes = 'espadas_ouros_paus_copas'.split('_') # separa as palavras retornando uma lista
print(naipes)

cartas = [Carta(valor, naipe) for naipe in naipes
                               for valor in valores]

#print(cartas)
#__________________________________________________________________________________________________

# 25 - Classe - Baralho

from random import choice

class Baralho:
    valores = [str(n) for n in range(2, 11)] + (list('JQKA'))
    naipes = 'espadas_ouros_paus_copas'.split('_')

    def __init__(self):
        self.cartas = cartas = [Carta(valor, naipe) for naipe in naipes
                               for valor in valores]

    def __len__(self): # retornar o tamanho
        return len(self.cartas)

    def __getitem__(self, posicao): # pegar posição
        return self.cartas[posicao]


# ACESSANDO ELEMENTOS ATRAVÉS DA CLASSE baralho:
baralho = Baralho()

print(len(baralho))

print(baralho[0]) # acessando primeira carta.

print(baralho[-1]) # acessando última carta.

print(choice(baralho)) # sorteando carta

# Slicing

print(baralho[:3]) # Vai pegar os três primeiras cartas.

print(baralho[12::13]) # vai pular de treze em treze pegado todos os "A".

print(baralho[11::13]) # vai pegar todos os "K" reis do baralho.

print(baralho[::-1]) # acessando o baralho invertido.

# ITERAR COM O IN:
#descobrir se uma carta está no baralho:

'''Carta('4', 'bolinhas') in baralho
print(True)'''




