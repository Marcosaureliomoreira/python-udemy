class computador:
    pass

pc1 = computador()
pc2 = computador()
pc3 = computador()
print(type(pc1))
print(type(pc2))
print(type(pc3))

pc1.cor = 'branco'    #atributos
pc2.cor = 'azul'      #atributos
pc3.cor = 'preto'     #atributos

print(pc1.cor)
print(pc2.cor)
print(pc3.cor)

print('-' * 20)

pc1.hd = 500
pc2.hd = 1000
pc3.hd = 350

print(pc1.hd)
print(pc2.hd)
print(pc3.hd)

print('-' * 20)

print(pc1.cor, pc1.hd)

class retangulo:                      # Alguns dos formatos de se fazer atributos.
    pass

ret1 = retangulo()
ret2 = retangulo()

ret1.altura = 20
ret2.largura = 10

ret1.largura = 40
ret2.altura = 30
print(ret1.altura * ret1.largura)
print(ret2.altura * ret2.largura)

#======================================================================================================================

