from random import randint
from time import sleep
ganhou = 0
print('-=-' * 5, 'Jogo do Par ou Ímpar'.upper(), '-=-' * 5)
while True:
    while True:
        player_p_i = str(input('Par ou ímpar? [P/I]')).strip()[0]
        if player_p_i in 'PpiI':
            break
        else:
            print('Humm, eu não sei o que significa isso, tente de novo :)')
    player = int(input('Digite seu número: '))
    cpu = randint(0, 10)
    print('Hmm...')
    sleep(.5)
    print('Lá vamos nós e...')
    sleep(1)
    soma = player + cpu
    if soma % 2 == 0 and player_p_i in 'Pp' or soma % 3 == 0 and player_p_i in 'Ii':
        print(f'Eu joguei o {cpu} e você {player}. A soma deu {soma}...')
        print('Me ganhou dessa vez... Parabéns')
        ganhou += 1
        print('Vamos de novo...')
    else:
        print(f'Eu joguei o {cpu} e você {player}. A soma deu {soma}...')
        print(f'Você perdeu com {ganhou} vitórias...')
        break
print('Quem sabe na próxima... Até mais.')
sleep(1)
print('Fui')

