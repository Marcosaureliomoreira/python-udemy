
#Pandas

#pip install pandas
import pandas as pd

dicionario = {"dados":[
    {
        "altura": 1.59,
        "ativado": False,
        "email": None,
        "usuario": "ana"
    },
    {
        "altura": 1.81,
        "ativado": True,
        "email": "pedrinho@email.com",
        "usuario": "pedro"
    },
{
        "altura": 1.59,
        "ativado": False,
        "email": None,
        "usuario": "ana"
    },
    {
        "altura": 1.81,
        "ativado": True,
        "email": "pedrinho@email.com",
        "usuario": "pedro"
    },
{
        "altura": 1.59,
        "ativado": False,
        "email": None,
        "usuario": "ana"
    },
    {
        "altura": 1.81,
        "ativado": True,
        "email": "pedrinho@email.com",
        "usuario": "pedro"
    },
{
        "altura": 1.59,
        "ativado": False,
        "email": None,
        "usuario": "ana"
    },
    {
        "altura": 1.81,
        "ativado": True,
        "email": "pedrinho@email.com",
        "usuario": "pedro"
    }

]}

#print(dicionario["dados"])

#Transformando os dados em DataFrame:
data = pd.DataFrame(dicionario["dados"])
#print(data)

#--------------------------------------------------

#Convertendo o arquivp acima para "csv" que vai poder ser aberto por uma planilha do excel, vai criar um arquivo.
#"index=False" significa que não vai mostrar os números ao lado, como no exemplo acima.
data.to_csv('cadastro.csv', index=False)

#-----------------------------------------------------------------------------------------------------------------------

#Lendo CSV e manipulando DataFrames:

#Ler arquivo CSV:

cadastro = pd.read_csv('cadastro.csv')
#print(cadastro)# <<< mostrando na tela

#Mostrando os cinco primeiros elementos, posso controlar colocando entre parênteses o quanto quero mostrar ex: (2) << dois ultimos elementos.
#print(cadastro.head())

#Vai mostrar os quatro ultimos elementos, posso controlar colocando entre parênteses o quanto quero mostrar ex: (2) << dois ultimos elementos.
#print(cadastro.tail())

#Selecionando apenas uma coluna:
#print(cadastro['altura'])

#Selecionando apenas uma coluna e somando com o método "sum":
#print(cadastro['altura'].sum())

#Selecionando apenas uma coluna e verificando a média com o método "mean":
#print(cadastro['altura'].mean())

#Selecionando apenas uma coluna e verificando o desvio padrão com o método "mean":
#print(cadastro['altura'].std())

#Selecionando apenas uma coluna e verificando quais elementos de repetem método "mode":
#print(cadastro['altura'].mode())

#Selecionando apenas uma coluna e contando quantos elementos possui com o metodo "count":
#print(cadastro['altura'].count())

#Deletando registro com o método "drop":
#"inplaca=True" tem que ser passado para surtir efeito na ação.
print(cadastro.drop(index=2, inplace=True))
print(cadastro)
