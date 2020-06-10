def area(l, c):
    print('-' * 20)
    print('Dimensões')
    print('-' * 20)
    print(f'L: {l:.1f} m\n'
          f'C: {c:.1f} m')
    print(f'Área de {l*c:.1f} m²')


# Programa principal
area(float(input('Largura do terreno: ')), float(input('Comprimento do terreno: ')))
