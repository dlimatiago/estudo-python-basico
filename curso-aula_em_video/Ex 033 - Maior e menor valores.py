n = (int(input('1° valor: ')), int(input('2° valor: ')), int(input('3° valor: ')))
if n[0] > n[1] and n[0] > n[2]:
    maior = n[0]
if n[1] > n[0] and n[1] > n[2]:
    maior = n[1]
if n[2] > n[0] and n[2] > n[1]:
    maior = n[2]
if n[0] < n[1] and n[0] < n[2]:
    menor = n[0]
if n[1] < n[0] and n[1] < n[2]:
    menor = n[1]
if n[2] < n[0] and n[2] < n[1]:
    menor = n[2]
print('O maior foi {} e o menor foi {}.'.format(maior, menor))