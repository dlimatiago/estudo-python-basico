num = []
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('\033[1;34mNúmero adicionado com sucesso!\033[m')
    else:
        print('\033[1;31mEsse número já foi adicionado!\033[m')
    ans = str(input('Deseja adicionar outro número? [S/N] ')).strip()[0]
    if ans in 'nN':
        break
print('-=-' * 15)
num.sort()
print(f'Os números digitados foram {num}')