# Periodos de Tempo (Freq)
import pandas as pd
import locale

# locale serve para trabalhar com dados em português.
# Traduzindo para português: Vai traduzir os meses para português.
locale.setlocale(locale.LC_ALL, 'pt-BR') # windows
#locale.setlocale(locale.LC_ALL, 'pt-BR.utf8') # linux

inicio = '01-01-2020'
fim = '31-12-2020'

import pandas

# "date_range' é um range de datas.
# "MS" significa início do mês. portanto vai mostrar o primeiro dia de cada mês.
# "strftime('%B de %Y')" converte e mostra o nome dos meses e o ano.
x = pd.date_range(inicio, fim, freq='MS').strftime('%B de %Y')
print(x)







                                    # String Para Periodos (Freq)

#Alás         Descição
# B           Frquêcia de dias úteis
# C           Frquência de dias úteis personalizados
# D           Frequência do dia do calendário
# W           Frequência semanal
# M           FrequÊncia de final do mês
# SM          frequência final semestral(15 e final do mês)
# BM          frequência final do mês útil
# CBM         frequência de final de mês comercial personalizada
# MS          frequência de início do mês.

