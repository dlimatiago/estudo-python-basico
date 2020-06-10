matriz, line = [], []
for linha in range(1, 4):
    for coluna in range(1, 4):
        line.append(int(input(f'Digite um valor para [{linha},{coluna}]: ')))
    matriz.append(line[:])
    line.clear()
print('-=-' * 10)
for i in matriz:
    for j in range(3):
        print(f'[ {i[j]:^5} ]', end=' ')
    print()