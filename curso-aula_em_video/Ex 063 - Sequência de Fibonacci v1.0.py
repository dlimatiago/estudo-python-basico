print("""----------------------------------------------------
               SEQUÊNCIA DE FIBONACCI
----------------------------------------------------""")
n = int(input('Quantos termos você quer ver? '))
n1, n2, cont = 0, 1, 3
print('\n{} → {}'.format(n1, n2), end='')
while cont <= n:
    fib = n1 + n2
    print(' → {}'.format(fib), end='')
    n1 = n2
    n2 = fib
    cont += 1
print(' → FIM')