def contador(inicio, final, passo):
    from time import sleep as pausa
    final = final + 1 if final > inicio else final - 1
    passo = 1 if passo == 0 else passo
    passo = abs(passo) if final > inicio else -passo

    print(f'Contagem de {inicio} até {final} de {passo} a {passo}:')
    pausa(2.5)
    for n in range(inicio, final, passo):
        print(f'{n}', end=' ')
        pausa(.5)
    print('FIM')
    print('-' * 30)


# Programa principal
print('-' * 30)
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))

