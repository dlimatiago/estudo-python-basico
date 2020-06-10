stuff = ('Blusa', 'Bermuda', 'Calça', 'Cueca', 'Casaco', 'Tênis')
price = ('29,90', '59,90', '119,90', '12,99', '179,99', '200,00')
print('=' * 45)
print('Loja das Brusinhas'.center(45))
print('=' * 45)
for item in range(6):
    print(f'{stuff[item]:.<30}', end='')
    print(f' R${price[item]:>7}')
print('=' * 45)