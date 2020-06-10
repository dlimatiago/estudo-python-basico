numbers, posmax, posmin = list(), list(), list()
for n in range(5):
    numbers.append(int(input(f'Digite o valor da posição \033[1;32m{n}\033[m:')))
maxi, mini, c = max(numbers), min(numbers), 0
while True:
    if c == len(numbers):
        break
    elif maxi == numbers[c] and c < len(numbers):
        posmax.append(c)
    elif mini == numbers[c] and c < len(numbers):
        posmin.append(c)
    c += 1
print(f'A lista de números informadas foi: {numbers}')
print(f'O maior número é o {maxi}', 'nas posições ' if len(posmax) > 1 else 'na posição ', end='')
for key in posmax:
    print(key, end='...')
print()
print(f'O menor númeor é o {mini}', 'nas posições ' if len(posmin) > 1 else 'na posição ', end='')
for keys in posmin:
    print(keys, end='...')