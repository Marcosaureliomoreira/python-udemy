
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
    }

]}

#print(dicionario["dados"])

#Transformando os dados em DataFrame:
data = pd.DataFrame(dicionario["dados"])
print(data)

#--------------------------------------------------

#Convertendo o arquivp acima para "csv" que vai poder ser aberto por uma planilha do excel, vai criar um arquivo.
#"index=False" significa que não vai mostrar os números ao lado, como no exemplo acima.
data.to_csv('cadastro.csv', index=False)

#-----------------------------------------------------------------------------------------------------------------------

