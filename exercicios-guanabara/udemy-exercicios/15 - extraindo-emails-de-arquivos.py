#Extraindo emails de arquivos de texto

texto = """
Texto antes
ga_to@gamil.com
pa-to@yahoo.com
No meio alguns textos
pata1995@meu-email.eu
rato2020@hotmail.com
k@email.net
E depois alguns textos
"""


#Escrevendo texto:
'''with open('email.txt', 'w') as f:
    f.write(texto)


#Lendo texto:
with open('email.txt', 'r') as f:
    for n, linha in enumerate(f, 1): # numerando as linhs do arquivo.
        print(f'{n}: {linha}', end='')
'''


#Retirando somente os emails com a expressão regular:
'''import re
f = open('so_emails.txt', 'w')  #escrevendo
p = re.compile(r'[\w-]+@[\w-]+\.\w+')
with open('email.txt') as emails:
    for linha in emails:
        for match in p.finditer(linha):
            print(match.group())
            f.write(match.group()+'\n')
f.close()'''


#Testando para ver se o arquivo "so_email" esta funcionando.
with open('so_emails.txt') as so_email:
    for email in so_email:
        print(email, end='')
