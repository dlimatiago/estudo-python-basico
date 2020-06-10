even, odd, allnum = [], [], []
while True:
    number = int(input('Digite um número: '))
    allnum.append(number)
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
    ans = str(input('Deseja continuar?[S/N] ')).strip()[0]
    if ans in 'nN':
        break
print('-=-' * 20)
print(f'Lista completa: \033[34m{allnum}\033[m\n'
      f'Lista dos pares: \033[33m{even}\033[m\n'
      f'Lista dos ímpares: \033[31m{odd}\033[m')