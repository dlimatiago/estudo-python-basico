soma = 0
controle = 0
for i in range(3, 501, 2):
    if i % 3 == 0:
        controle += 1
        soma += i
print('A soma dos {} números ímpares múltiplos de 3 é {}.'.format(controle, soma))
