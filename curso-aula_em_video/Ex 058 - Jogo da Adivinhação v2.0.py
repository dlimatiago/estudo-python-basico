from random import randint
from time import sleep
print('-=-'*30)
print('Olá, eu sou o seu computador. Vamos brincar?')
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('-=-'*30)
n, tentativa = randint(0, 10), 1
r = int(input('Em que número eu pensei? '))
print('processando...'.upper())
sleep(.5)
if r == n:
    print(f'NA MOSCA!!! Eu realmente pensei no número {n} e ganhou com apenas {tentativa} tentativa')
else:
    while r != n:
        if r > n:
            print('Humm tente algo menor...')
            r = int(input('Você tem mais uma chance, diga-me sua resposta: '))
        elif r < n:
            print('Humm tente algo maior...')
            r = int(input('Você tem mais uma chance, diga-me sua resposta: '))
        tentativa += 1
    print(f'UAU, eu pensei no {n} desde o início parabéns!!!'
          f' Demorou {tentativa} vezes, mas você conseguiu!!!')