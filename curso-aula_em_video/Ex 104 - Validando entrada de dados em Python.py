def leiaint(n):
    while True:
        value = input(f'{n}')
        status = value.isnumeric()
        if status is True:
            return int(value)
        else:
            print('\033[1;4;31mEntrada inválida!\033[m')


# Main code
number = leiaint('Digite um número: ')
print(f'Você acabou de informar o número {number}.')