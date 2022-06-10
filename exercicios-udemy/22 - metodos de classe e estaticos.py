import datetime
class Funcionario():
    aumento = 1.04
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


    def dados(self):
        return {'nome': self.nome, 'salário': self.salario}

    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento

    # MÉTODO DE CLASSE:
    @classmethod
    def definir_novo_aumento(cls, novo_aumento): # "cls" é a própria classe Funcionario.
        cls.aumento = novo_aumento

    # MÉTODO ESTÁTICO:
    @staticmethod # Não exige nenhum argumento da classe "Funcionário".
    def dia_util(dia):
        # segunda-feira = 0
        # sábado = 5
        # domingo = 6
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True



Funcionario.definir_novo_aumento(1.05)
fabio = Funcionario('Fábio', 7000)
fabio.aplicar_aumento() # Chamando a função aplicar aumento.
print(fabio.dados())

pedro = Funcionario('Pedro', 8000)
pedro.aplicar_aumento()
print(pedro.dados())

# chamando a função para verificar se é dia útil.
minha_data = datetime.date(2019, 4, 13) # sábado
print(Funcionario.dia_util(minha_data))
