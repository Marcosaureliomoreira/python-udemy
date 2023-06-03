import os

# MOSTRANDO INFORMAÇÕES DO SISTEMA:
sistema = os.environ
#print(sistema)

# ACESSANDO O USUÁRIO DENTRO DO SISTEMA ATRAVÉS DE UM DICIONÁRIO
#print(sistema['USERNAME'])

# TRABALHANDO COM PASTAS:

# mostra onde está o conteúdo/caminho
#print(os.getcwd())

#CRIANDO UMA PASTA:
#os.mkdir("Teste")

# LISTANDO OS DIRETÓRIOS/ARQUIVOS PRESENTES NA ATUAL PASTA:
#print(os.listdir())

# CRIANDO DIRETÓRIOS EM CASCATA (um dentro do outro):
#caminho = r'C:\Users\morei\PycharmProjects\pythonexercicios\udemy-poo\biblioteca OS\2021\janeiro\manhã'
#os.makedirs(caminho)

# Listando os diretório/arquivos atuais
#print(os.listdir())

# REMOVENDO/APAGANDO PASTA (sempre será removida a pasta do final do caminho e se a pasta estiver vazia):
#os.rmdir(r'C:\Users\morei\PycharmProjects\pythonexercicios\udemy-poo\biblioteca OS\2021\janeiro\manhã')


                                    #TRABALHANDO COM ARQUIVOS

# os.startfile() => vai abrir o arquivo do tipo txt
#os.startfile(r'C:/Users/morei/OneDrive/Área de Trabalho/arq.txt')

#os.rename() => RENOMEANDO ARQUIVOS
#os.chdir(r'C:/Users/morei/OneDrive/Área de Trabalho') # => MOSTRANDO O CAMINHO DO ARQUIVO A SER ALTERADO (OBRIGATÓRIO)
#os.rename('arq.txt', 'arquivo_job.txt') # => renomeando o arquivo para: "arquivo_job"

# os.remove() => REMOVER ARQUIVO
# os.remove('nome_do_arquivo a ser removido.txt')

# os.walk() => PARECIDO COM O listdir(), MOSTRA AS RAÍZES DE UMA PASTA(ROOT), ARQUIVOS(FILES), DIRS(MOSTRA A PASTA E SE TEM ALGO DENTRO), ETC COMO NO EXEMPLO ABAIXO.
'''for root, dirs, files in os.walk(os.getcwd()):
    print(dirs)'''

#exemplo2 os.walk():
#for root, dirs, files in os.walk(r'C:/Users/morei/OneDrive/Área de Trabalho'): # => VAI MOSTRAR TUDO QUE ESTÁ NO CAMINHO AO LADO.
    #print(root)  vai mostrar as pastas dentro do caminho
    #print(dirs)  #vai mostrar todas as pastas que tem no caminho
    #print(files) # vai mostrar todos os arquivos que tem dentro de tal caminho


#Caminhos (submodos os.path)
#os.path.basename -> vai me permitir pegar o nome da pasta que estou no momento
#print(os.path.basename(os.getcwd())) # -> mostra o nome da pasta que estou no momento


# os.path.commonpath()-> pastas ou caminho em comum
caminho1 =r'C:\Users\morei\PycharmProjects\pythonexercicios\udemy-poo'
caminho2 =r'C:\Users\morei\PycharmProjects\pythonexercicios\udemy-poo\biblioteca OS'
#print(os.path.commonpath([caminho1, caminho2])) -> vai mostrar as pastas ou caminho em comum
#print(os.path.commonprefix([caminho1, caminho2])) # -> vai mostrar textos/strings em comun


# OS.PATH.DIRNAME()
# print(os.path.dirname(caminho1)) -> vai mostrar o caminho da pasta que estou.


# OS.PATH.JOIN() -> permite a criação de um caminho para mudar de pasta.
drive = "C:"
usuario = "morei"
pasta_base = "Área de Trabalho"

caminho = os.path.join(drive, r'\Users', usuario, 'OneDrive', pasta_base)
os.chdir(caminho)

print(os.getcwd())