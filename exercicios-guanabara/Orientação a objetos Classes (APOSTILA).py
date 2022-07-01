'''class conta:
    pass

    #Em outro arquivo
    from conta import conta
    conta = conta()
    print(type(conta))
    #<class '_main_.Conta'>
    conta.titular = 'João'
    print(conta.titular)
    conta.saldo = 120.0
    print(conta.saldo)'''





class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print('Inicializando uma conta'.center(40))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite



    def deposita(self, valor):
        self.saldo += valor


    def saca(self, valor):
        self.saldo -= valor


    def extrato(self):
        print(f'Número: {self.numero}\nSaldo: {self.saldo}')



conta = Conta('123-4', 'João', 120.0, 1000.0)
conta.deposita(20.0)
conta.extrato()
conta.saca(15)
conta.extrato()


def saca(self, valor):
    if self.saldo < valor:
        return False
    else:
        self.saldo -= valor
        return True
