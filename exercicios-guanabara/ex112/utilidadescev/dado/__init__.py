def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[31mERRO: \"{entrada}\" é um preço inválido!\033[m' )
        else:
            válido = True
            return float(entrada)