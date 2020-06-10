num = (
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: '))
)
count_nine = num.count(9) if int('9') in num else '0'
none = c = 0
while c <= 3:
    if num[c] == 3:
        pos_three = c + 1
        break
    elif c == 3:
        none = 1
    c += 1
print(f'A quantidade de vezes que o 9 apareceu foi {count_nine}')
print(f'O 3 apreceu na {pos_three}ª posição' if none == 0 else 'Não tem 3 entre os valores')
print('Os números pares encontrados:', end=' ')
for par in num:
    if par % 2 == 0:
        print(f'{par}', end=' ')
        c += 1
    elif c == 0 and par == num[3]:
        print('Não há pares')