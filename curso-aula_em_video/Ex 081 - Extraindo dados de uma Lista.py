numbers = []
while True:
    numbers.append(int(input('Digite um número: ')))
    answ = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if answ in 'n':
        break
print('-=-' * 20)
numbers.sort(reverse=True)
print(f'Você digitou {len(numbers)} elementos.\n'
      f'Os valores em ordem decrescente são {numbers}')
print('\033[31;1mO valor 5  não foi encontrado na lista!\033[m' if int("5") not in numbers
      else '\033[34;4mO valor 5 faz parte da lista!\033[m')