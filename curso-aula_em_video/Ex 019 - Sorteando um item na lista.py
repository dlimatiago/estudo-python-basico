from random import choice
alunos = [
    input('Nome do primeiro aluno: '),
    input('Nome do segundo aluno: '),
    input('Nome do terceiro aluno: '),
    input('Nome do quarto aluno: ')
]
print('O aluno sorteado foi {}.'.format(choice(alunos)))
