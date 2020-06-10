from time import sleep
from random import randint
print('''Suas opções são:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Sua jogada: '))
if 3 > jogador > -1:
    cpu = randint(0, 2)
    opções = ('PEDRA', 'PAPEL', 'TESOURA')
    """print('JO')
    sleep(1)
    print('KEN...')
    sleep(2)
    print('PÔ')
    sleep(1)"""
    print('-=-' * 8)
    print('Jogador jogou {}\nCPU jogou {}'.format(opções[jogador], opções[cpu]))
    print('-=-' * 8)
    if cpu == 0:
        if jogador == 0:
            print('EMPATE')
        if jogador == 1:
            print('JOGADOR VENCE')
        if jogador == 2:
            print('CPU VENCE')
    if cpu == 1:
        if jogador == 0:
            print('CPU VENCE')
        if jogador == 1:
            print('EMPATE')
        if jogador == 2:
            print('JOGADOR VENCE')
    if cpu == 2:
        if jogador == 0:
            print('JOGADOR VENCE')
        if jogador == 1:
            print('CPU VENCE')
        if jogador == 2:
            print('EMPATE')
else:
    print('\033[31mVocê escolheu uma opção inválida\033[m')


