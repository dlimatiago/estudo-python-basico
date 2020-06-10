from statistics import mean
from time import sleep
name, grade = [], []
answer = 0
while True:
    name.append(str(input('Nome: ').strip().capitalize()))
    grade.append([float(input('Nota 1: ')), float(input('Nota 2: '))])
    ans = str(input('Quer continuar ? [S/N] ')).strip()[0]
    if ans in 'Nn':
        print('-=-' * 26)
        break
print(f'{"N°":<4}', f'{"NOME":<10}', f'{"MÉDIA":>8}')
print('-' * 36)
for item in range(len(name)):
    media = mean(grade[item])
    print(f'{item:<4}{name[item]:<10}{media:>8.1f}')
print('-' * 35)
while answer != 999:
    answer = int(input('Mostra notas de qual aluno? (999 interrompe) '))
    if answer == 999:
        break
    print(f'Notas de {name[answer]} são {grade[answer]}')
    print('-' * 35)
print('Finalizando...'.upper())
sleep(2)
print('<< volte sempre >>'.upper())