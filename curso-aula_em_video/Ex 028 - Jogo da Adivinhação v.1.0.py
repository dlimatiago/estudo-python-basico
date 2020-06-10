from random import randint
from time import sleep
print('-=-'*30)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-'*30)
n = randint(0, 5)
r = int(input('Em que número eu pensei? '))
print('processando...'.upper())
sleep(2)
if n == r:
    print(f'VOCÊ GANHOU!!! Eu realmente pensei no número {n}')
else:
    print(f'EU GANHEI!!! Eu pensei no número {n} não no {r}')

