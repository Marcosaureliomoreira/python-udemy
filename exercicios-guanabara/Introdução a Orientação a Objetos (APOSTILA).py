'''conta = {'numero': '123-4', 'titular': 'João', 'saldo': 120.0, 'limite': 1000.0}
conta2 = {'numero': '123-5', 'titular': 'José', 'saldo': 200.0, 'limite': 1000.0}'''


def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta


conta1 = cria_conta('123-4', 'João', 120.0, 1000.0)
conta2 = cria_conta('123-5', 'José', 200.0, 1000.0)


# FINCIONALIDADES
#Podemos depositar um valor em uma conta. Vamos criar uma função para representar esta funcionalidade, além do depósito
# precisamos saber qual conta irá receber o valor.
'''
def deposita(conta, valor):
    conta['saldo'] += valor     #conta['saldo'] = conta['saldo'] + valor



def saca(conta, valor):
    conta['saldo'] -= valor



def extrato(conta):
    #print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))
    print(f'numero: {conta["numero"]}, \nsaldo: {conta["saldo"]}')


conta = cria_conta('123-4', 'João', 120.0, 1000.0)
deposita(conta, 15.0)
extrato(conta)
print('-' * 20)
saca(conta, 20.0)
extrato(conta)
'''





'''def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta



def deposita(conta, valor):
    conta['saldo'] += valor
    

def saca(conta, valor):
    conta['saldo'] -= valor
    
    
def extrato(conta):
    print(f'Numero: {conta["numero"]}, \nsaldo: {conta["saldo"]}')


conta = cria_conta('123-7', 'João', 500.0, 1000.0)
deposita(conta, 50.0)
extrato(conta)
saca(conta, 20.0)
extrato(conta)'''




#Criação da conta
def criar_conta(numero, titular, saldo, limite):
    conta = {'número': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta


conta3 = criar_conta('135-7', 'João', 100.0, 1000.0)
conta4 = cria_conta('135-8', 'Marcos', 200.0, 1000.0)


#Funcionalidades para a conta:
def depositar(conta, valor):
    conta['saldo'] += valor


def saque(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    print('Novo Saldo:')
    print(f'Número: {conta["numero"]}\nSaldo: {conta["saldo"]}')



conta = cria_conta('123-8', 'Marcos', 200.0, 1000.0)
depositar(conta, 100.0)
extrato(conta)
saque(conta, 100.0)
print('-' * 20)
extrato(conta)


