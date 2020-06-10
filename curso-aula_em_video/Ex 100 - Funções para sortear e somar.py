from random import randint as ri


def sorteia(l):
    for i in range(5):
        l.append(ri(1, 10))
    print(f'Sorteando 5 valores aleatórios da lista: ', end='')
    for numb in l:
        print(f'{numb}', end=' ')
    print('PRONTO!')


def somapar(lst):
    soma = 0
    for n in lst:
        soma = soma + n if n % 2 == 0 else soma + 0
    print(f'Somando os valores pares de {lst}, temos {soma}.')


# Programa principal
lista = list()
sorteia(lista)
somapar(lista)
