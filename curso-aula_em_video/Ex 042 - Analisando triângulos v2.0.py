m1 = float(input('Digite a 1° medida: '))
m2 = float(input('Digite a 2° medida: '))
m3 = float(input('Digite a 3° medida: '))
if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m1 + m2:
    print('Essas medidades PODEM FORMAR UM TRIÂNGULO ', end='')
    if m1 == m2 == m3:
        print('{}EQUILÁTERO{}'.format('\033[4;32m', '\033[m'))
    elif m1 == m2 or m2 == m3 or m3 == m1:
        print('{}ISÓSCELES{}'.format('\033[4;33m', '\033[m'))
    else:
        print('{}ESCALENO{}'.format('\033[4;34m', '\033[m'))
else:
    print('Essas medidas não podem formar um triângulo')
