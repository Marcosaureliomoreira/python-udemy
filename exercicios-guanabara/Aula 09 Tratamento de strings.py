frase = ('Curso em vídeo python')
#print(frase[9:21:2])   <<<< Vai de 9 até 21 pulando de dois em dois.
#print(frase[:5])       <<< Vai fatiar do 0 até o 5.
#print(frase[9::3])     <<< vai fatiar do 9 ate o final pulando de três em três.
#print(len(frase))      <<< Análisa quantos caracteres há dentro da variável frase.
#print(frase.count('e')) <<< Analisa quantas vezes aparece a letra dentro da frase.
#print(frase.count('o', 0, 13)) <<< Analisa já com o fatiamento quantas vezes há a letras o de 0 até 13.
#print(frase.find('deo'))  <<< vai analisar em que momento começa a palavra 'deo' na variável frase.
#print(frase.find('android'))  <<< Quando se é colocado um valor que não existe dentro de uma frase(string), é retornado o valor -1.
#print('Curso' in frase)   <<< Verifica se existe a palavra curso na string "frase" e retorna o TRUE OU FALSE.
#print(frase.replace('python', 'android'))  <<< Irá substituir a palavra "python" por "android".
#print(frase.upper()) <<< Tranforma mínúsculas em maiúsculas.
#print(frase.lower()) <<< Transforma maiúsculas em minúsculas.
#print(frase.capitalize()) <<< Mantém apenas a primeira letra de uma frase(string) em MAIUSCÚLA.
#print(frase.title()) <<< Tranforma a primeira letra de uma frase em "MAISCÚLA" EXEMPLO: Curso Em Video Python.
#print(frase.strip())  <<< Remove Todos os espaços inúteis de uma string, do começo e do final, mantando apenas o espaço do meio.
#print(frase.rstrip())  <<< Remove todos os espaços da direita de uma string.
#print(frase.lstrip())  <<< Remove todos os espaços á esquerde de uma string.
#print(frase.split())  <<< Vai dividir/separar as palavras de uma frase(string) a partir dos espaços.
#print('-'.join(frase)) #<<< Vai juntar todos os caractéres a partir de traços ou espaços, o que estiver entre parênteses. e pode separar também.
#print({frase.index("python")})  <<< irá localizar em que posição se encontra a palavra python.
#frase.isspace()    #EXEMPLO: frase = (' ') <<< verífica se há carcteres em branco na frase e retorna False ou True.
#print(frase.center(50))  <<< Centraliza a quantidade de caracteres que está entre parênteses.
#print(frase.endswith('E')) # <<< Este método retorna True se a string terminar com o valor especificado. como no exemplo ao lado.
'''frase2 = str(input('Diga onde esta aprendendo python que completaremos a frase: ')).lower()
frase = 'Estou Assistindo {} para aprender tudo sobre programação'.title()
print(frase.format(frase2))'''


