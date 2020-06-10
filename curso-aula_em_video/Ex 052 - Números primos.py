cont = 0
n = int(input('Digite um número: '))
for t in range(1, n+1):
    if n % t == 0:
        cont += 1
        t = '\033[31m{}\033[m'.format(t)
    print('\033[33m{}\033[m'.format(t), end=' ')
if cont == 2:
    print('\nO número {} é PRIMO, pois possui 2 divisores.'.format(n))
elif cont != 2:
    print('\nO número {} NÃO É PRIMO, pois possui {} divisores '.format(n, cont))

