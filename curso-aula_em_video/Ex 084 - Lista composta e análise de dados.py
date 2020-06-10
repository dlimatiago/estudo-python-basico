people, infos, nameheavy, namelight = [], [], [], []
while True:
    infos.append(str(input('Nome: ')).strip())
    infos.append(float(input('Peso: ')))
    people.append(infos[:])
    infos.clear()
    answ = str(input('Deseja continuar? [S/N]')).strip()
    if answ in 'nN':
        break
for i in range(len(people)):
    if i == 0:
        heaviest = people[i][1]
        nameheavy.append(people[i][0])
        lightiest = people[i][1]
        namelight.append(people[i][0])

    if people[i][1] > heaviest and i != 0:
        heaviest = people[i][1]
        nameheavy.pop()
        nameheavy.append(people[i][0])
    elif people[i][1] == heaviest and i != 0:
        nameheavy.append(people[i][0])
    if people[i][1] < lightiest and i != 0:
        lightiest = people[i][1]
        namelight.pop()
        namelight.append(people[i][0])
    elif people[i][1] == lightiest and i != 0:
        namelight.append(people[i][0])
print('-=-' * 15)
print(f'Ao todo você cadastrou {len(people)} pessoas.')
print(f'As pessoas mais pesadas pesam {heaviest} Kg e seus nomes são {nameheavy}')
print(f'As pessoas mais leves pesam {lightiest} Kg e seus nomes são {namelight}')
