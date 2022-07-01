

#                                           Simulação de caixa eletrônico
# =======================================================================================================================
'''from time import sleep
valor = 0
conta = 300
novaopção = 0
novaopção2 = ' '
cancel = ' '
erro = 0
senha = 1020
frase = 'BANCO 24 HORAS'
print(frase.center(50))
num = int(input('Pressione um número para começar... '))
senha = int(input('Digite a senha: '))
while senha != 1020:
    senha = int(input('Digite a senha novamente: '))
    erro += 1
    if erro == 2:
        print('Cartão BLOQUEADO!')
        print('Voce excedeu o número de tentativas. Procure uma agência mais próxima.')
        break

if senha == 1020:
        print('1- SAQUE\n2- SALDO \n3- CANCELAR A OPERAÇÃO')
        print('-'*22)
        opção = int(input('O que deseja fazer? '))
        print('=' *22)
        if opção == 1:
            valor = int(input('Quanto deseja sacar? '))
            print('=' *22)
            if 0 <= valor <= 300:
                print('Saque permitido')
                print('AGUARDE PARA A RETIRADA DO DINHEIRO...')
                sleep(3)
                print('Retire o dinheiro!')
                sleep(3)
                print('Obrigado por utilizar os caixas eletrônicos. VOLTE SEMPRE!')
            else:
                print('Valor não autorizado')
                while valor > 300:
                    novaopção = int(input('Digite um novo valor ou um número negativo para cancelar a operação: '))
                    if novaopção < 0:
                        print('OPERAÇÃO CANCELADA!')
                        sleep(2)
                        print('Aguarde...')
                        sleep(3)
                        print('SESSÃO ENCERRADA!')
                        break
                    if 0 <= novaopção <= 300:
                        print('Saque permitido')
                        print('AGUARDE PARA A RETIRADA DO DINHEIRO...')
                        sleep(3)
                        print('Retire o dinheiro!')
                        sleep(3)
                        print('Obrigado por utilizar os caixas eletrônicos. VOLTE SEMPRE!')
                        break
        elif opção == 2:
            valor = conta
            print(f'O seu saldo é de: {valor}')
            while novaopção2 not in 'SN':
                novaopção2 = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
                if novaopção2 == 'N':
                    print('Aguarde...')
                    sleep(3)
                    print('Fim')
                    break
                if novaopção2 == 'S':
                    print('1 - SAQUE\n2- SALDO \n3- CANCELAR A OPERAÇÃO')
                    print('-' * 22)
                    opção = int(input('O que deseja fazer? '))
                    print('=' * 22)
                    if opção == 1:
                        valor = int(input('Quanto deseja sacar? '))
                        print('=' * 22)
                        if 0 <= valor <= 300:
                            print('Saque permitido')
                            print('AGUARDE PARA A RETIRADA DO DINHEIRO...')
                            sleep(3)
                            print('Retire o dinheiro!')
                            sleep(3)
                            print('Obrigado por utilizar os caixas eletrônicos. VOLTE SEMPRE!')
                        else:
                            print('Valor não autorizado!')
                            while valor > 300:
                                novaopção = int(input('Digite um novo valor ou um número negativo para cancelar a operação: '))
                                if novaopção < 0:
                                    print('OPERAÇÃO CANCELADA!')
                                    sleep(2)
                                    print('Aguarde...')
                                    sleep(3)
                                    print('SESSÃO ENCERRADA!')
                                    break
                                if 0 <= novaopção <= 300:
                                    print('Saque permitido')
                                    print('AGUARDE PARA A RETIRADA DO DINHEIRO...')
                                    sleep(3)
                                    print('Retire o dinheiro!')
                                    sleep(3)
                                    print('Obrigado por utilizar os caixas eletrônicos. VOLTE SEMPRE!')
                                    print('Fim')
                                    break
        elif opção == 3:
            while cancel not in 'SN':
                print('Operação cancelada.')
                print('Aguarde...')
                print('Obrigado e volte sempre!')
                sleep(4)
                break'''
# =====================================================================================================================

# =======================================================================================================================
'''lista = [[], []]
for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor %2 == 0:
        lista[0].append(valor)
    elif valor %2 == 1:
        lista[1].append(valor)
print(f'Os valores completos da lista é {lista}')
lista[1].remove()
print(f'A lista com os valores pares é {sorted(lista[0])}')
lista[1].sort(reverse=True)
print(f'A lista com os valores ímpares em forma descrescente é {lista[1]}')'''
# =======================================================================================================================


'''tabela = ['leite', 'arroz', 'milho']
for i in tabela:
    print(f'\nEm {i} temos as vogais: ' , end='')
    for v in i:
        if v in 'aeiou':
            print(f'{v }', end='')'''

'''somapar = somacol = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a cada posição [{l},{c}] '))
        if matriz[l][c] %2 == 0:
            somapar += matriz[l][c]


for l in range(0, 3):
    somacol += matriz[l][2]
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma de todos os valores pares é {somapar}')
print(f'A soma de todos os valores da terceira coluna é {somacol}')'''

'''lista = [[], []]

for c in range(1, 8):
    n = int(input('Digite um número: '))
    if n %2 == 0:
        lista[0].append(n)
    elif n %2 == 1:
        lista[1].append(n)
lista[0].sort()

print(f'Os números pares digitados foram: {lista[0]}')
print(f'Os números ímpares digitados foram: {lista[1]}')
print(f'Na lista de números ímpares foram encontrados {len(lista[1])} elementos.')
print(f'O número 5 se encontra {lista[1].count(5)} vezes')'''

'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número para a posição: [{linha}, {coluna}]'  ))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()'''


'''def soma(a, b):
    soma = a + b
    print(f'A soma das idades {idade1} + {idade2} = {soma}')




idade1 = int(input('Digite a Primeira idade: '))
idade2 = int(input('Digite a segunda idade: '))
soma(idade1, idade2)'''




'''def escreva(frase):
    tam = len(frase)
    print('=' * tam)
    print(frase)
    print('=' * tam)




escreva('Marcos Aurélio Moreira Dores')'''



'''def diminuir(valor):
    diminuir = valor - 1
    print(f'O resultado é {n} = {diminuir}')


n = int(input('Digite um número: '))
diminuir(n)'''

'''def linha():
    print('-' * 30)
from time import sleep
def contador(*i, fim, pas):
    contador = i
    for n in contador:
        sleep(0.5)
        print(f'{n}', end=' ')
     print()'''



'''from time import sleep
def contador(i, f, p):
    print(f'A contagem de {i} até {f} de {p} em {p}')
    cont = i
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('Fim')
    else:
        if cont > f:
            cont = i
            while cont >= f:
                print(f'{cont}', end=' ')
                sleep(0.5)
                cont -= p
            print('Fim')'''
# ======================================================================================================================
'''contv = cont_A = 0
palavras = ('cao',
            'gato',
            'barata',
            'elefante',
            'leao',
            'peixe',
            'gorila',
            'tigre',
            'tubarao')

print(palavras)

for p in palavras:
    print(f'\nNa palavra {p} temos as vogais: ', end='')
    for v in p:
        if v in 'aeiou':
            contv += 1
            if 'a' in v:
                cont_A += 1
            print(f'{v}', end='')
print(f'\nA quantidade de vogais existentes é: {contv}')
print(f'A letra A aprece {cont_A}')'''
#=======================================================================================================================
'''def linha():
    print('-=' * 25)

lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [Digite apenas S ou N] ')).upper().strip()[0]
    if op == 'N':
        break
linha()
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista de valores de forma decrescente é: {lista}')
if 5 in lista:
   print('O número 5 esta na lista. ')
else:
   print('O número 5 não foi encontrado. ')
print(f'O número 5 aparece {lista.count(5)} vezes.')'''

'''from time import sleep

def maior(* num):
    cont = maior = 0
    print(f'\nAnalizando os valores...')
    for valor in num:
        print(f'{valor} ', end=' ')
        sleep(0.4)
        if cont == 0:
            valor = maior
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores.')
    print(f'O maior valor informado foi {maior}')




maior(1, 3, 6, 4, 9)
maior(3, 4, 6, 10)
maior(6)'''


'''i = int(input('Digite um número: '))
fim = int(input('Digite o número final: '))
passo = int(input('Digite o passo: '))
from time import sleep
if i < fim:
    cont = i
    while cont <= fim:
        print(f'{cont}', end=' ')
        sleep(0.4)
        cont += passo
elif i > fim:
    cont = i
    while cont >= fim:
        print(f'{cont}', end=' ')
        sleep(0.4)
        cont -= passo'''


'''def soma(a, b):
    s = a + b

    print(s)


soma(1, 2)'''

'''from datetime import datetime, date

def c_idade(atual, nasc):
    idade = atual - nasc
    print(f'Você tem {idade} anos.')

atual = (date.today().year)
nasc = int(input('Nascimento: '))
c_idade(atual, nasc)'''




'''def media(n1, n2):
    m = n1 + n2 / 2
    print(f'A média de {n1} e {n2} é {m}')



n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número'))
media(n1, n2)'''










#num = int(input('Digite um número para calcula a sua calculadora: '))
#for c in range(1, 11):
#    print(f'{num} x {c} = {num*c}')


'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(1, 3, 4)
r2 = somar(2, 4, 10)
r3 = somar(1)
print(f'Os resultados foram {r1} {r2}, {r3}')'''


def linha():
    print('-=' * 30)

'''pessoas = dict()
galera = list()
cont = maior = menor = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Digite o Nome: '))
    pessoas['idade'] = int(input('Idade: '))
    cont += 1
    if cont == 0:
        maior = pessoas['idade']
    else:
        if pessoas['idade'] > maior:
            maior = pessoas['idade']
    galera.append(pessoas.copy())
    linha()
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? ')).upper().strip()[0]
    if op == 'N':
        break
    linha()
print(galera)
print(f'A quantidade de pessoas cadastrados foi {cont}. ', end='')
while cont == 1 and op == 'N':
    #print(f'Foi cadastrada apenas {cont} idade.')
    break
for p in galera:
    if cont > 1:
        print(f'{p["nome"]} ', end=' ')

print(f'\nA maior idade digitada foi {maior} anos. de ', end='')

for p in galera:
    if p['idade'] == maior:
        print(f'{p["nome"]}.', end=' ')
print('\n<<FIM>>')'''
#=======================================================================================================================
'''
def linha2():
    print('-' * 32)
c_idade = 0
from datetime import datetime, date
linha()
print('                 CÁLCULO ELEITORAL  ')
linha()
while True:
    nascimento = int(input('Digite o ano do seu Nascimento: '))
    if nascimento <= 0 or nascimento == 999:
        print('Ano de nascimento não informado.')
        print('<<<FIM>>>')
        break
    mês = int(input('Digite o do mês do seu nascimento: '))
    linha2()
    idade = datetime.now().year - nascimento
    if nascimento < 2004 and 1 <= mês <= 12:
        print(f'Você Já atingiu a maior idade e está ápto para votar! você tem {idade} anos.')
        linha()
    elif nascimento == 2004 and mês >= 10:
        print(f'Você Já atingiu a maior idade e está ápto para votar!')
    elif nascimento == 2004 and mês < 10:
        print(f'Você ainda irá completar {idade} anos de idade, portanto ainda não está ápto para votar.')
    else:
        if nascimento > 2004:
            c_idade = 18 - idade
            print(f'Você ainda não está ápito para votar! você tem {idade:.0f} anos')
            print(f'Falta {c_idade} anos para o início de sua votação.')
            linha()'''
#=======================================================================================================================

'''def c_idade(nasc):
    from datetime import datetime, date
    idade = datetime.now().year - nascimennto
    print(f'Você nasceu no ano de {nascimennto}, a sua idade é {idade} anos.')


nascimennto = int(input('Nascimento: '))
c_idade(nascimennto)'''



'''def fatorial(num, show=False):
    """
    Calcula o valor do fatorial
    :param num: O número a ser calculado.
    :param show: (Opcional) Mostra o calculo do fatorial.
    :return: Retorna o valor do fatorial.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
#help(fatorial)'''



'''def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')


n = str(input('O nome do jogador: '))
g = str(input('Quantos gols ele marcou? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)'''



'''def leiaint(msg):
    certo = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            certo = True
            valor = int(n)
        else:
            print('\033[31mERRO! Digite um valor inteiro válido.\033[m')
        if certo:
            break
    return valor




n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o númer {n}')'''






'''n = str(input('Digite um número: '))
ok = False
valor = 0'''
#=======================================================================================================================
                                       # Teste com o método "is numeric"
'''def linha():
    print('-=' * 30)


cont = maior = menor = cont_n = 0
while True:
    valor = 0
    n = str(input('Digite um número: '))
    if n.isnumeric():
        valor = int(n)
        cont += 1
        if valor == 10:
            cont_n += 1
        if cont == 1:
            maior = menor = valor
        else:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
        tipo = ' '
        while tipo not in 'SN':
            tipo = str(input('Deseja continuar? [S/N] ')).upper().strip()
        if tipo == 'N':
            break
    else:
        print('\033[31mERRO! Digite apenas números\033[m')
linha()
print(f'A quantidade de valores digitados foram: {cont}')
print(f'O maior número digitado foi: {maior}')
print(f'menor valor digitado foi: {menor}')
if valor == 10:
    print(f'O número 10 foi encotrado na lista e aparece {cont_n} vezes.')
else:
    print('O número 10 não foi encontrado na lista.')'''
#=======================================================================================================================
def tamanho(linha):
    tam = len(linha)
    print('-=' * tam)

'''linha = ('Deseja continuar')

cont = maior = menor = 0
lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um número na pos {c+1} ')))
    tamanho(linha)
    if cont == 0:
        maior = menor = lista
print(lista)
print(f'O maior número foi {max(lista)} na posição: ', end='')
for pos, v in enumerate(lista):
    if v == max(lista):
        print(f'{pos+1}', end='')
print(f'\nO menor valor digitado foi {min(lista)}. na posição: ', end='')
for pos, v in enumerate(lista):
    if v == min(lista):
        print(f'{pos+1}', end='')'''


'''from time import sleep
for c in range(0, 21):
    if c != 18:
        print(c, end=' ')
        sleep(0.1)
    else:
        break'''



#=======================================================================================================================
                                               #Descobridor de senha
'''senha = int(input('Digite sua senha cinco digitos: '))

from time import sleep
for c in range(0, 100000):
    if c != senha:
        print(c, end=' ')
        sleep(0)
    else:
        print(f'Senha encontrada \033[31m{c}\033[m.')
        break'''
#=======================================================================================================================

'''listanum = list()
maior = menor = cont = 0
for c in range(1, 6):
    num = int(input('Digite um número: '))
    listanum.append(num)
listanum.sort()
print(listanum)'''





'''while True:
    n = str(input('Digite um número: '))
    if n.isnumeric():
        print(f'O número digitado foi: {n}')
        break
    else:
        print(f'\033[31mErro!\033[m')
'''


'''def imc_calc(peso, altura):
        imc = peso / (altura ** 2)
        print(f'Seu IMC é de {imc:.1f}')
        if imc < 18.5:
            print('Você esta ABAIXO DO PESO normal')
        elif 18.5 <= imc < 25:
            print('PARABÉNS, você esta na sua faixa de PESO NORMAL')
        elif 25 <= imc < 30:
            print('Você está em SOBREPESO')
        elif 30 <= imc < 40:
            print('Você está em OBESIDADE')
        elif imc >= 40:
            print('Você está em OBESIDADE MÓRBIDA, cuidado!')

p = float(input('Digite Seu peso: '))
alt = float(input('Digite sua altura: '))
print(imc_calc(p, alt))'''









#=======================================================================================================================
'''lista = list()
for c in range(1, 3):
    lista.append(str(input('Nome: ')).upper().strip())
    lista.append(int(input('Idade: ')))
print(lista)
desejo = str(input('Deseja mostrar a idade de quem? ')).upper().strip()
if desejo in lista:
    if desejo in lista[0]:
        print(f'A idade de {desejo} é {lista[1]} anos')
    elif desejo in lista[2]:
        print(f'A idade de {desejo} é {lista[3]} anos')
'''
#=======================================================================================================================
def linha():

    print('-' * 30)

'''from random import randint
jogador = tentativa = pedra = papel = tesoura = 0

computador = randint(1, 3)
print('<<<Vamos jogar Jokenpô>>>'.center(40))
#print('1. para PEDRA \n2. para PAPEL \n3. para TESOURA')
linha()
jogador = int(input('O que deseja jogar? '))
if jogador == 1:
    print('Deu pedra!')
elif jogador == 2:
    print('Deu papel')
elif jogador == 3:
    print('Deu Tesoura!')

print(computador)
'''




'''if jogador == 1 and computador == 2:
    print(f'Deu PAPEL, VENCI')
    print(f'Eu joguei {computador}')
elif jogador == 2 and computador == 3:
    print(f'Eu venci')
    print('Deu TESOURA')
    print(f'Eu joguei {computador}')
elif jogador == 3 and computador == 1:
    print('Eu venci!')
    print('Deu PEDRA')
    print(f'Eu joguei {computador}')
else:
    print('Você venceu!')
    print(f'Eu joguei {computador}')'''


'''lista = ['pedra', 'papel', 'tesoura']
from random import randint

computador = randint(0, 2)
print('<<<Vamos jogar Jokenpô>>>'.center(40))
print('0. para PEDRA \n1. para PAPEL \n2. para TESOURA')
linha()
jogador = int(input('O que deseja jogar? '))
linha()
print(f'jogador jogou {lista[jogador]}')
print(f'Computador jogou {lista[computador]}')
linha()
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador Vence!')
    elif jogador == 2:
        print('Computador Vence!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')'''



'''from random import choice

lista = ['p', 'a', 'c']
print(choice(lista))'''

'''try:
    num1 = int(input('Número: '))
    num2 = int(input('Número: '))
    soma = num1 + num2
except (ValueError, TypeError):
    print('Digite apenas números!')
except KeyboardInterrupt:
    print('Dados não inseridos!')
else:
    print(f'A soma é {soma}')
finally:
    print('Obrigado! Volte sempre!')'''



'''soma = cont = 0
try:
    for c in range(1, 3):
        num = int(input('Digite um número: '))
        soma += num
except ValueError:
    print('Digite apenas números')
except KeyboardInterrupt:
    print('Dados não inseridos!')
else:
    print(f'A soma dos números é {soma}')
finally:
    print('Obrigado! Volte sempre!')'''
#=======================================================================================================================
'''cont = num = desejo = 0
while True:
    try:
        num = int(input('Número: '))
        cont += 1
    except (ValueError, TypeError, IndexError):
        print('\033[31mERRO: digite apenas números Inteiro válidos\033[m')
    except KeyboardInterrupt:
        print('Dados não inseridos')
    else:
        op = str(input('Deseja continuar? ')).upper().strip()[0]
        while op not in 'SN':
            op = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if op == 'N':
            break


print(f'Foram digitados {cont} números')'''




import locale

'''while True:
    try:
        num = float(input('Numero: '))
    except (ValueError, TypeError):
        print('\033[31mERRO: Digite um número real:\033[m ')
    else:
        print(f'O número digitado foi {num}')
        break'''

'''def numReal(msg):
    while True:
        try:
            num = float(input(msg))
        except (TypeError, ValueError):
            print('ERRO!')
        else:
            return num



n = numReal('Numero: ')
print(f'O numero digitado foi {n}')'''







def conversorvirg(nome):
    palavra = nome.replace('.', ',')
    return palavra












'''senha = int(input('Senha: '))
for c in range(0, 1000000000000000000):
    if senha == c:
        print(f' Senha encontrada: \033[31m{senha}\033[m')
        break
    else:
        print(f'{c}', end=' ')'''









#=======================================================================================================================



'''class cliente:
    def __init__(self, nome, ano_nasc, tel):
        self.nome = nome
        self.ano_nasc = ano_nasc
        self.tel = tel



cl1 = cliente('André', 1980, 222)
cl2 = cliente('Alice', 1940, 333)
cl3 = cliente('Maria', 1930, 555)


print('O ano de nascimento de' , cl1.nome, 'é', cl1.ano_nasc)
print('O telefone do cliente é', cl2.tel, 'e seu nome é', cl2.nome)'''




'''def sorteio(num):
    from random import randint
    num = randint(0, 3)
    return num


n = int(input('Digite um Número entre 0 e 3: '))
print(f'Você digitou o número {n}')
print(f'Foi sorteado o número: {sorteio(None)}')'''



'''def leiaStr(msg):
    while True:
        n = str(input(msg)).upper().strip()
        if n.isnumeric() or n in (',', '.', ':'):
            print('ERRO!')
        else:
            return n

def c_conta(nome, cpf):
    conta = {'nome': nome, 'cpf': cpf}

    return conta

#conta1 = c_conta('Marcos', 123.45)
#conta2 = c_conta('Mariana', 123.54)

n = leiaStr('Digite seu nome completo: \033[37m(sem acentos)\033[m ')
cpf = int(input('CPF: '))
print(c_conta(n, cpf))'''
#-----------------------------------------------------------------------------------------------------------------------

'''def leiaString(frase):
    while True:
        nome = str(input(frase)).replace('.', ',')
        if nome.isalpha() == True:
            print('ERRO:')
        else:
            return nome


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO!')
        else:
            return n


num = leiaString('Número: ')
num2 = leiaString('Número: ')'''



'''n = float(input('Número: '))
print(f'O número foi {n.__ceil__()}')'''


'''class Funcionario:
    def __init__(self, nome, idade, bairro):
        self.nome = nome
        self.idade = idade
        self.bairro = bairro

    def meubairro(self):
        print('O bairro é', self.bairro)

f = Funcionario('Mariana', 30, 'Catete')

print(f.nome,)
f.meubairro()'''





'''menor = 0
cont = 0
for c in range(0, 3):
    n = int(input('Num: '))
    cont += 1
    if cont == 1:
        menor = n
    else:
        if n < menor:
            menor = n
print(f'O menor é {menor}')'''



'''from datetime import date

atualAno = date.today().year
atualMes = date.today().month
cont_m = 0
nasc = int(input('Ano de Nascimento: '))
idade = atualAno - nasc
m = int(input('Mês de nascimento: '))
if m > 12:
    m = 1
elif m <= 0:
    print('Mês inválido')
dia = int(input('Dia: '))
dia = m - atualMes

if atualMes < m:
    idade -= 1
    cont_m = m + atualMes
elif atualMes == m:
    cont_m = 0
print(f'Você tem {idade} anos, {cont_m} meses e {dia} dias.')'''





'''def virgila(nome):
    resp = nome.replace('.', ',')
    return resp


n = str(input('Nome: '))
print(virgila(n))'''




'''def soma(a, b):
    resp = a + b
    print(f'A soma é {resp}')


n1 = int(input('Numero: '))
n2 = int(input('Número: '))
soma(n1, n2)'''




'''t1 = 0
t2 = 1
cont = 0
print(f'{t1}, {t2}', end='')
cont += 1
while cont <= t2:
    t3 = t1 + t2'''




#Verificando números em comun em duas listas
'''def inteiro(txt):
    while True:
        try:
            n = int(input(txt))
        except (TypeError, ValueError):
            print('ERRO: Digite números')
        except(KeyboardInterrupt):
            print('ERRO!')
        else:
            return n


num1 = list()
num2 = list()
numcomun = list()
for c in range(1, 4):
    n = inteiro('Número: ')
    num1.append(n)
for c in range(1, 4):
    n2 = inteiro('Número: ')
    num2.append(n2)
print(num1)
print(num2)

for i, n in enumerate(num1 + num2):
    print(f'Na posição:{i+1} temos o número: {n}')
print('Os números em comun são: ', end=' ')
for numero in num1 and num2:
    if numero in num1 and numero in num2:
        print(numero, end=' ')
if numero not in num1 and num2 or numero not in num1 + num2:
    print('\033[31mNão há\033[m')'''




'''def leiaSexo(sexo):
    while True:
        sexo = str(input('Sexo: ')).upper()
        if sexo not in 'FM':
            sexo = str(input('Sexo: ')).upper()
        else:
            break'''


'''def soma(a, b, c):
    s = a + b + c
    return s'''



'''def leiaLetras(txt):
    while True:
        nome = str(input(txt)).strip()
        if nome.isnumeric() == True:
            print('ERRO: Digite apenas letras.')
        else:
            return nome


def leiaInteiro(txt):
    while True:
        try:
            n = int(input(txt))
        except (TypeError, ValueError):
            print('ERRO: Digite apenas números inteiros')
        else:
            return n

def leiaCPF(txt):
    while True:
        n = str(input(txt)).rstrip('-.')
        if n.isnumeric() == True:
            return n
        else:
            print('ERRO! Digite apenas números sem espaços ou outro caractere.')



cadastro = dict()

cadastro['nome'] = leiaLetras('Nome: ')
cadastro['idade'] = leiaInteiro('Idade: ')
cadastro['cpf'] = leiaCPF('CPF: \033[37m(Sem espaços) \033[m')

print(cadastro)'''




#-----------------------------------------------------------------------------------------------------------------------


'''class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def alterar(self, novaidade):
        self.idade = novaidade






funcionario = Pessoa('Angela', 22, 'F')
print('Nome:', funcionario.nome)
print('Idade:', funcionario.idade)
print('Sexo:', funcionario.sexo)

funcionario.alterar(10)
print('Idade:', funcionario.idade)'''



import re


'''def exressaoReg(msg):
    e = re.compile(r'[a-z-A-Z-à-ù0-9@._]+')
    f = e.findall(msg)
    for l in f:
        print(l, end=' ')


exressaoReg("""
Marcos_Aurélio1995@hotmail.com

""")'''

import sys


'''def exressaoRegnum(msg):
    e = re.compile(r'[0-9]+')
    f = e.findall(msg)
    for l in f:
        print(l, end=' ')


exressaoRegnum("""
Marcos
""")'''






'''def arq(ar):
    a = [].append(ar)
    for n in set(ar):
        print(n)



b = arq(['carro', 'casa', 'casa', 'casa', 'pc', 'carro'])'''


from random import randint
'''import re

contatos = {'nome': 'Marcos', 'Tel': '2222-3333'}

print(contatos)

ct = """
nome': 'Marcos', 'Tel': '2222-3333,
nome': 'Hugo', 'Tel': '4444-3333
"""

c = re.compile(r'[\w+-]+')
e = c.findall(ct)
print(e)'''


'''from time import sleep
from random import randint
num = [2, 4, 1, 44, 30, 99, 86]
num.sort()
print(num)
l = []
l_regressiva = []
for n in num:
    if n == 44:
        for c in range(0, 21):
            if c % 2 == 0:
                continue
            print(c, end=' ')
            sleep(0.1)
            l.append(c)
print('FIM!\nIniciando contagem regressiva.')
sleep(2)
if len(l) >= 10:
    for r in range(21, 0, -1):
        print(r, end=' ')
        sleep(0.1)
        l_regressiva.append(r)

print('\nREINICIO:')
s = randint(1, 30)
print(s)
if s in l_regressiva:
    print('\033[35mO número sorteado esta na contagem regressiva.\033[m')
else:
    print('\033[31mInfelizmente o número soretado não está na lista.\033[m')'''



#msg = ('Olá mundo como vcs estão?')
#print(msg[0:9])



'''def remover_A(msg):
    l = []
    n = str(input(msg))
    l.append(n)
    for c in l:
        if 'a' in c:
            print(c.replace('a', '-'))
    for c in l:
        if 'A' in c:
            print(c.replace('A', '-'))






frase = remover_A('Frase: ')'''



'''def inverso(dados):
    for i in range(len(dados)-1, -1, -1):
        yield dados[i]

for e in inverso('Marcos'):
    print(e, end='')'''


class Pessoas:
    def __init__(self):
