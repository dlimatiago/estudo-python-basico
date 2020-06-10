player, gol = dict(), list()

player['Nome'] = str(input('Nome do Jogador: ')).strip().title()
matches = int(input(f'Quantas partidas {player["Nome"]} jogou? '))

for part in range(matches):
        gol.append(int(input(f'Quantos gols na partida {part+1}? ')))

player['Gols'] = gol
print('-=-' * 30)
print(player)

print('-=-' * 30)
for chave, valor in player.items():
    print(f'O campo {chave} tem a informação {valor}')

print('-=-' * 30)
print(f'O jogador {player["Nome"]} jogou {matches} partidas.')
for partida, gol in enumerate(player['Gols']):
    print(f'     ==> Na partida {partida+1}, {player["Nome"]} fez {gol} gols.')
