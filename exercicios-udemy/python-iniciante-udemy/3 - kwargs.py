
# *args ==> argumentos
# **Kwargs ==> kwords arguments (argumentos de palavra-chave)

'''def args_kwargs(*args, **kwars):
    print(args)
    print(kwars)

# vai imprimir: que os args são uma tupla e os kwars são: dicionário.
args_kwargs('um', 2, 3, 0, True, nome='Pedro', idade=29, status='Online')'''

#OBS: Os "kwargs" não podem vir antes dos "args"

#-----------------------------------------------------------------------------------------------------------------------

# Desempacotando kwargs de dicionários:

def formata_hota(horas, minutos='00', segundos='00'):
    print(f'{horas}:{minutos}:{segundos}')


tempo = {
    'horas': '15',
    'minutos': '10',
    'segundos': '54'
}

print(tempo)

formata_hota(**tempo) # << Desempacotando

