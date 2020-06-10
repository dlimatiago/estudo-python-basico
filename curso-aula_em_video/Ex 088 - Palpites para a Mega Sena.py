from random import randint
from time import sleep
print('\033[1;31m*\033[m' * 25)
print('JOGA NA MEGA SENA'.center(25))
print('\033[1;31m*\033[m' * 25)
game = list()
ans = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=-  SORTEANDO {ans} JOGOS -=-=-=-')
for n in range(ans):
    aux = list()
    while True:
        numero = randint(1, 60)
        if numero not in aux:
            aux.append(numero)
        if len(aux) == 6:
            break
    aux.sort()
    game.append(aux)
    print(f'Jogo {n + 1}: {game[n]}')
    sleep(1)
    aux.clear()
print('-=-=-=-=-=- < BOA SORTE! > -=-=-=-=-=-')
