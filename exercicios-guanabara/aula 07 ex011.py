larg = float(input('Largura de parede: '))
alt = float(input('Altura de parede: '))
area = larg * alt
print('Sua parede tem a a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, area))
tinta = area /2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))