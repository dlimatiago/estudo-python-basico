player, gols, time = dict(), list(), list()
while True:
    player['Nome'] = str(input('Nome do Jogador: ')).strip().title()
    matches = int(input(f'\tQuantas partidas {player["Nome"]} jogou? '))
    for part in range(matches):
        gols.append(int(input(f'\tQuantos gols na partida {part+1}? ')))

    while True:
        resp = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
        if resp in 'sn':
            break
        else:
            print('\033[1;31mOpção inválida!\033[m')
    player['Gols'] = gols[:]
    time.append(player.copy())
    gols.clear()
    if resp == 'n':
        break
print('-=-' * 30)
print(f'{"Cod ":<3}', f'{"Jogador":<15}', f'{"Gols":<15}', f'{"Total":>20}')
print('-' * 60)
for cod, dic in enumerate(time):
    print(f'{cod:<3}{dic["Nome"]:<15}{str(dic["Gols"]):<15}{sum(dic["Gols"]):>20}')

while True:
    while True:
        opc = int(input("Analisar os dados de algum jogador? (999 para finalizar) "))
        if opc == 999 or opc in range(len(time)):
            break
        else:
            print('\033[1;31mOpção inválida! Não há jogadores com esse código\033[m')
    if opc == 999:
        break
    
    print(f'ESTATÍSTICAS DO JOGADOR {time[opc]["Nome"]}:')
    for i, item in enumerate(time[opc]["Gols"]):
        print(f'\t - No jogo {i+1} fez {item} {"gols." if item > 1 else "gol."}')

