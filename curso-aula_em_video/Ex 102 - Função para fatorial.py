def fatorial(n=1, show=False):
    """
    > Calcula o Fatorial de um número n.
    :param n: número inteiro positivo maior ou igual a 1. n=1 as default.
    :param show: Parâmetro lógico para mostrar ou não o cálculo do fatorial. False as default.
    :return: O valor do fatorial de n com ou sem processo ou retorna uma mensagem de erro para um n inválido.
    """
    from math import factorial as f
    if n >= 1:
        if show is False:
            print('-'*30)
            return f(n)
        else:
            print('-'*30)
            print(f'{n}! = ', end='')
            for i in range(n, 1, -1):
                print(f'{i} x', end=' ')
            print('1 = ', end='')
            return f(n)

    else:
        return print('\033[1;31mEsse valor é incorreto, consulte o help(fatorial)\033[m')


num = int(input('Digite um número para saber seu fatorial: '))
s = bool(input('Deseja mostrar a conta? [True: Sim False: Não] '))
print(fatorial(num, s))
