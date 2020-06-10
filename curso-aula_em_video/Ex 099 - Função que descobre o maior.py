def maior(*value):
    if len(value) != 0:
        print('Analisando os valores passados...')
        for number in value:
            print(f'{int(number)}', end=' ')
        print(f'Foi informado {len(value)} {"valores" if len(value) > 1 else "valor"}.')
        print(f'O maior achado foi o {int(max(value))}.')
    else:
        print('\033[1;31mnone\033[m')
    print('-=-' * 20)


# Programa principal
print('-=-' * 20)
maior(2, 3, 5, 90.98, 6, 57, 101, 12)
maior(1, 3, 1)
maior(-5, -10, -20)
maior(0, -1, 12, -50)
maior(3, 2, 1, 5, 3, 2)
maior(5)
maior()
