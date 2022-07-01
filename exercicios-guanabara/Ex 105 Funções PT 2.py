#Faça Um programa que tenha uma função chamada notas() que pode receber várias notas de um aluno e vai retornar um dicionário com
# as seguintes informações:

#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- Situação (opcional)

def notas(*n, sit=False):
    """
    Função para salvar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    alunos = dict()
    alunos['total'] = len(n)
    alunos['maior'] = max(n)
    alunos['menor'] = min(n)
    alunos['media'] = sum(n) / len(n)
    if sit and alunos['media'] >= 7:
        alunos['situação'] = 'Boa'
    elif sit and 5 <= alunos['media'] < 7:
        alunos['situação'] = 'Regular'
    elif sit and alunos['media'] < 5:
        alunos['situação'] = 'Ruim'
    #print(alunos)
    return alunos



resp = notas(8, 9.8, 6.5, 9, 2, 4, sit=True)
#print(resp)
help(notas)




