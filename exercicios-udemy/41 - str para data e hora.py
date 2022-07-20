# String para DataHora (Strptime)
import datetime

str_data_hora = '18-04-2021 15:39:41'
#print(str_data_hora)

# trabalhando com (Strftime)
convertida = datetime.datetime.strptime(str_data_hora, '%d-%m-%Y %H:%M:%S')
#print(convertida)

#-----------------------------------------------------------------------------------------------------------------------

                                                #String para Data

str_data = '27-09-2022'
data = datetime.datetime.strptime(str_data, '%d-%m-%Y').date()
#print(data)

#-----------------------------------------------------------------------------------------------------------------------

                                                 # String para tempo
#MANEIRA 1:
'''str_tempo = '15:32:49'
tempo = datetime.datetime.strptime(str_tempo, '%H:%M:%S').time()
print(tempo)'''

# MANEIRA 2:
str_tempo = '15 horas, 32 minutos e 49 segundos'
tempo = datetime.datetime.strptime(str_tempo, '%H horas, %M minutos e %S segundos')
print(tempo)

                                                #String Para Tempo (Strftime) tabela
#</tr>

# %a - Dia da semana como nome abreviado da localidade.                       Exemplo:   Seg
# %A - Dia da semana com o nome completo da localidade.                       Exemplo:   Segunda-feira
# %w - Dia da semana com um número decimal, onde 0 é domingo. e 6 é sábado.   Exemplo:   1
# %d - Dia do mês como um numero decimal preenchido com zero.                 Exemplo:   30
# %-d - Dia do mês como un número decim. (Específico da plataforma)           Exemplo:   30
# %b - Mês como nome abreviado da localidade                                  Exemplo:   Set
# %B - Mês como nome completo do código do idioma.                            Exemplo:   Setembro
# %m - Mês como um número decimal preenchido com zero.                        Exemplo:   09
# %-m  Mês como um número decimal. (Especifico da plataforma)                 Exemplo:   9
# %y - Ano sem século como um número decimal preenchido com zero.             Exemplo:   13
# %Y - Ano com o século com o número decimal.                                 Exemplo:   2013
# %H - Hora (relógio de 24 horas) como um numero decimal preenchido com zero. Exemplo:   07
