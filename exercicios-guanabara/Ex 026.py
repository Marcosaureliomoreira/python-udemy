nome = str(input('Digite uma frase:')).lower().strip()
print('A letra a aparece?{}vezes'.format(nome.count('a')))
print('Ela aparece pela primeira vez na posição: {}'.format(nome.find('a')+1))
print('Ela aparece pela ultima vez na posição:{}'.format(nome.rfind('a')+1))








