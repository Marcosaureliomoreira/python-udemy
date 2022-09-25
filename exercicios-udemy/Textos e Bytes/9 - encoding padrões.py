# Encodings Padrões (default)

import sys, locale

# abaixo teremos como resposta qual encoding está em cada local do sistema operacional
comandos = """
locale.getpreferredencoding(),
f.encoding,
sys.stdout.encoding,
sys.stdin.encoding,
sys.stderr.encoding,
sys.getdefaultencoding(),
sys.getfilesystemencoding()
"""

# verificando o encoding preferido do sistema operacional:
#print(locale.getpreferredencoding())

# o "eval" é uma função builtin que executa o comando que está entre string pra gente:
eval('locale.getpreferredencoding()')

# dividindo a lista de comandos acima:
print(comandos.split())

# verificando o encoding de cada comando da lista comandos:
# r.just() => significa alinhamento a direita, também tem l.just que é a esquerda.
for comando in comandos.split():
    print(f'{comando.rjust(29)}', eval(comando))
