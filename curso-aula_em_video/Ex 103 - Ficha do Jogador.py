def ficha(nome='<desconhecido>', gol=0):
    nome = nome if nome.isalpha() else '<desconhecido>'
    return f'O jogador {nome} fez {gol} gol(s) no campeonato'


n = str(input('Nome do Jogador: '))
g = str(input('Número de gols: '))

print(ficha(n, gol=int(g)if g.isnumeric() else 0))