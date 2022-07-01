class computador:
    def __init__(self, cor, hd):
        self.cor = cor
        self.hd = hd


pc1 = computador('preto', 250)
pc2 = computador('vermelho', 500)
pc3 = computador('branco', 1000)

print(pc1.hd, pc1.cor)
print(pc2.hd, pc2.cor)
print(pc3.hd, pc3.cor)

