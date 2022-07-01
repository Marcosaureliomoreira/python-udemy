class Endereco:
    def __init__(self, cep,
                 rua=None,
                 numero=None,
                 casa=None,
                 bairro=None,
                 cidade=None):
        self.cep = cep
        self.rua = rua
        self.casa = casa
        self.numero = numero
        self.cidade = cidade
        self.bairro = bairro



class Pessoas:
    def __init__(self, nome, idade, email, *args, **kargs):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.obj_endereco = Endereco(*args, **kargs)            #como endereço possui muitas informações tivemos que colocar como um objeto e criar uma classe acima


ana = Pessoas('Ana', '28', 'ana@gmail.com', 24923034)
#=======================================================================================================================

                                                # AGREGAÇÃO


class Pessoas:
    def __init__(self, nome, idade, email, endereco):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.obj_endereco = endereco

ana_end = Endereco(249230334)
ana = Pessoas('Ana', '28', 'ana@gmail.com', ana_end)

print(ana.nome, ana_end.cep)
