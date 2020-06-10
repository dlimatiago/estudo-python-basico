n = int(input('Informe um número: '))
u, d, c, m = n // 1 % 10, n // 10 % 10, n // 100 % 10, n // 1000 % 10
print('Analisando o número {}\n'
      'Unidade: {}\n'
      'Dezena: {}\n'
      'Centena: {}\n'
      'Milhar: {}'.format(n, u, d, c, m))