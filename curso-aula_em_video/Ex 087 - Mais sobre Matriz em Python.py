matriz, line = [], []
for linha in range(1, 4):
    for coluna in range(1, 4):
        line.append(int(input(f'Digite um valor para [{linha},{coluna}]: ')))
    matriz.append(line[:])
    line.clear()
soma = soma3 = 0
for l in range(3):
    for c in range(3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            soma3 += matriz[l][c]
maior = max(matriz[1])
print('-=-' * 10)
for i in matriz:
    for j in range(3):
        print(f'[ {i[j]:^5} ]', end=' ')
    print()
print('-=-' * 10)
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da 3ª coluna é {soma3}')
print(f'O maior valor da 2ª linha é {maior}')