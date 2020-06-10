from statistics import mean as med

pessoa, dados = dict(), list()

while True:
    pessoa['Nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        else:
            print('\033[1;31mOpção iválida, digite novamente\033[m')
    pessoa['Idade'] = int(input('Idade: '))
    dados.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip()[0]
        if resp in 'SNsn':
            break
        else:
            print('\033[1;31mOpção iválida, digite novamente\033[m')
    if resp in 'nN':
        break

media = list()
for dic in dados:
    media.append(dic["Idade"])
media = med(media)

mulher = list()
for dicio in dados:
    if dicio['Sexo'] in 'fF':
        mulher.append(dicio['Nome'])

acima = list()
for dicion in dados:
    if dicion['Idade'] > media:
        acima.append(dicion['Nome'])

print('-=-' * 30)
print(f'{"Informações Úteis":^50}')
print(f'Pessoas cadastradas: {len(dados):>2} {" pessoas" if len(dados) > 1 else "pessoa"}')
print(f'Média da idade: {int(media):>8} anos')
print(f'Mulheres cadastradas: ', end='')
for m in mulher:
    print(f'{m}', end=' ')
print()
print(f'Acima da média: ', end='')
for a in acima:
    print(f'{a:>11}', end=' ')
print()