from random import randint
from time import sleep
from operator import itemgetter
"""dices = dict()
color = {
    'red': '\033[1;31m',
    'gre': '\033[1;32m',
    'yel': '\033[1;33m',
    'blu': '\033[1;34m',
    'pur': '\033[1;35m',
    'cya': '\033[1;36m',
    'close': '\033[m'
    }  # Cores dos jogadores

dices['p1'], dices['p2'] = randint(1, 6), randint(1, 6)
dices['p3'], dices['p4'] = randint(1, 6), randint(1, 6)

print('Players estão jogando...')
sleep(1.7)
print(f'{color["red"]}Player 1:{color["close"]} Tirei {color["red"]}{dices["p1"]}{color["close"]} no dado')
sleep(.8)
print(f'{color["gre"]}Player 2:{color["close"]} Eu tirei um {color["gre"]}{dices["p2"]}{color["close"]}...')
sleep(.9)
print(f'{color["yel"]}Player 3:{color["close"]} Ah, consegui um {color["yel"]}{dices["p3"]}{color["close"]} no dado!')
sleep(1)
print(f'{color["blu"]}Player 4:{color["close"]} Foi um {color["blu"]}{dices["p4"]}{color["close"]} no dado aqui...')
aux = list()
for k, item in dices.items():
    aux.append(item)
aux.sort(reverse=True)
pos = dict()
for obj in aux:
    for k, i in dices.items():
        if obj == i:
            pos[k] = obj
print(f'==={"Colocação":^15}===')
for k, v in enumerate(pos):
    print(f'{k+1}º lugar - {v:>4}')
    sleep(.5)
"""

dices, ranking = dict(), dict()
color = {
    'red': '\033[1;31m',
    'gre': '\033[1;32m',
    'yel': '\033[1;33m',
    'blu': '\033[1;34m',
    'pur': '\033[1;35m',
    'cya': '\033[1;36m',
    'close': '\033[m'
    }  # Cores dos jogadores

dices['p1'], dices['p2'] = randint(1, 6), randint(1, 6)
dices['p3'], dices['p4'] = randint(1, 6), randint(1, 6)

print('Players estão jogando...')
sleep(1.7)
print(f'{color["red"]}Player 1:{color["close"]} Tirei {color["red"]}{dices["p1"]}{color["close"]} no dado')
sleep(.8)
print(f'{color["gre"]}Player 2:{color["close"]} Eu tirei um {color["gre"]}{dices["p2"]}{color["close"]}...')
sleep(.9)
print(f'{color["yel"]}Player 3:{color["close"]} Ah, consegui um {color["yel"]}{dices["p3"]}{color["close"]} no dado!')
sleep(1)
print(f'{color["blu"]}Player 4:{color["close"]} Foi um {color["blu"]}{dices["p4"]}{color["close"]} no dado aqui...')
ranking = sorted(dices.items(), key=itemgetter(1), reverse=True)  # 1 para pegar valor, 0 para pegar chave
sleep(1)
print('==== RANKING ===='.center(30))
for p, i in enumerate(ranking):
    print(f'{p+1}° lugar: {i[0]} com {i[1]}.')

