times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio',
         'Athletico Paranaense', 'São Paulo', 'Internacional',
         'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco',
         'Atlético', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro',
         'Csa', 'Chapecoense', 'Avaí')
cor = ('\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[m', '\033[1;4m')
print(f'{cor[8]}Os 5 primeiros do Brasileirão:{cor[7]}', end=' | ')
for t in range(5):
    print(f'{cor[t]}{times[t]}{cor[7]}', end=' | ')
print()
print(f'{cor[8]}Os 4 últimos colocados do Brasileirão:{cor[7]}', end=' | ')
for ti in range(1, 6):
    print(f'{cor[-ti-3]}{times[-ti]}{cor[7]}', end=' | ')
print()
print(f'{cor[8]}Times do Brasileirão em ordem alfabética:{cor[7]}', end=' | ')
tim = c = 0
while tim < 20:
    if c < 7:
        c += 1
        print(f'{cor[c]}{times[tim]}{cor[7]}', end=' | ')
    else:
        c = 0
    tim += 1
print()
print(f'{cor[8]}Colocação do Chapecoense no Brasileirão:{cor[7]} '
      f'| {cor[4]}{times.index("Chapecoense")+1}ª posição{cor[7]} |')
