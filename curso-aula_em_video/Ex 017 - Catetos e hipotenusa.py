import math
'''co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
hp = sqrt(co**2 + ca**2)
print('O valor da hipotenusa é {:.1f}'.format(hp))'''

hp = math.hypot(float(input('Informe o valor do cateto oposto:')), float(input('Informe o valor do cateto adjacente: ')))
print('O valor da hipotenusa é {:.1f}'.format(hp))