real = float(input('Digite quanto você possui na sua carteira: R$ '))

dolar = 5.23
libra = 6.44
euro = 5.69

print(f'Cotação atual:\n R$ 1.00 = US$ {dolar}\n R$ 1.00 = € {euro}\n R$ 1.00 = £ {libra} ')
print()
print('Com R${:.2f} você pode comprar:\n US$ {:.2f}\n € {:.2f}\n £ {:.2f}'.format(real, real/dolar, real/euro, real/libra))






