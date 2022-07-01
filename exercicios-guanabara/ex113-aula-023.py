#Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número inválido.
# Aproveite e crie também a finção leiaFloat() com a mesma funcionalidade.



def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO: por favor digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar esse número:\033[m ')
            return 0
        else:
            return n



n1 = leiaInt('Digite um número Inteiro: ')
n2 = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real digitado foi {n2} ')
