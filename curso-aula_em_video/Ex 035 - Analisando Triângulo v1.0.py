from math import fabs
m1 = float(input('Digite a 1° medida: '))
m2 = float(input('Digite a 2° medida: '))
m3 = float(input('Digite a 3° medida: '))
if fabs(m2-m3) < m1 < m2+m3 and fabs(m1-m3) < m2 < m1+m3 and fabs(m1-m2) < m3 < m1+m2:
    print('Essas medidas podem formar um triângulo.')
else:
    print('Essas medidas não podem formar um triângulo')
