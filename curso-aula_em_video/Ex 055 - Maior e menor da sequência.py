maior = menor = 0
for p in range(1, 6):
    peso = float(input('Digite o {}° peso: '.format(p)))
    maior = peso if p == 1 or peso >= maior else maior
    menor = peso if p == 1 or peso <= menor else menor
print('O maior peso é {:.1f}Kg e o menor peso é {:.1f}Kg'.format(maior, menor))
