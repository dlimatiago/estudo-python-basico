largura = float(input('largura da parede: '))
altura = float(input('Altura da parede: '))
área = largura*altura
tinta = área/2

print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.1f} m².'.format(largura, altura, área))
print('Para pintar sua parede, você precisará de {:.1f}l de tinta.'.format(tinta))
