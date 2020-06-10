# Código de um fatorial com While
"""n = int(input('Informe um número para calcular seu fatorial: '))
cont1, cont2, cont, fat = n, n, 1, 1
while cont != n:
    cont += 1
    cont1 -= 1
    fat *= cont1
    if cont == n:
        fat *= n
print('Calculando {}! = {}'.format(n, fat))"""""

# Código de um fatorial com For
n = int(input('Informe um número para calcular seu fatorial: '))
f = 1
print('{}! = '.format(n), end='')
for x in range(n, 0, -1):
    print(f'{x}', end='')
    print(' x ' if x > 1 else ' = ', end='')
    f *= x
print(f'{f}', end='')
