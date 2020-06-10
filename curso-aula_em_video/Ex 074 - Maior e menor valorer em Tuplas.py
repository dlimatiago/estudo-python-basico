from random import sample, randint
cor = ('\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[m')
# num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
num = tuple(sample(range(10), 5))  # Forma mais simples. Gera uma tupla com de 5 elementos de 0 a 10
maior, menor = max(num), min(num)
print('Os números sorteados foram:', end=' ')
for n in range(5):
    print(f'{cor[n]}{num[n]}{cor[7]}', end=' ')
print()
print(f'O maior dos sorteados é o {cor[5]}{maior}{cor[7]}\n'
      f'O menor dos sorteados é o {cor[6]}{menor}{cor[7]}')