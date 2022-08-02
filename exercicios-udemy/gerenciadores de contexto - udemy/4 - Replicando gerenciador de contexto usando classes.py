
class Abrir:
    # recebendo o caminho completo do arquivo:
    def __init__(self, arquivo, modo):
        self.arquivo = arquivo
        self.modo = modo

    # função que faz o enter:
    def __enter__(self):
        self.arq = open(self.arquivo, self.modo)
        return self.arq

    # fechando o arquivo:
    def __exit__(self, tipo_exc, valor_exc, traceback):
        self.arq.close()


with Abrir('arquivos/exemplo2.txt', 'w') as f:
    f.write('Exemplo 2')

