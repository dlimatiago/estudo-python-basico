soma = 0
for x in range(1, 7):
    n = int(input('Digite {}° número: '.format(x)))
    if n % 2 == 0:
        soma += n
print('A soma dos pares informados é {}.'.format(soma))