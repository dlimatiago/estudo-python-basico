student = dict()

student['name'] = str(input('Nome do aluno: ')).strip().title()
student['grade'] = round(float(input(f'Média de {student["name"]}: ')), 1)
print('-=-' * 15)
if student['grade'] >= 6:
    student['situation'] = 'aprovado'
    print(f'- Aluno: {student["name"]}\n'
          f'- Média aluno: {student["grade"]}\n'
          f'- Situação: Aluno \033[1;34m{student["situation"]}\033[m')
elif 5.9 >= student['grade'] > 4.5:
    student['situation'] = 'recuperação'
    print(f'- Aluno: {student["name"]}\n'
          f'- Média aluno: {student["grade"]}\n'
          f'- Situação: Aluno de \033[1;33m{student["situation"]}\033[m')
else:
    student['situation'] = 'reprovado'
    print(f'- Aluno: {student["name"]}\n'
          f'- Média aluno: {student["grade"]}\n'
          f'- Situação: Aluno \033[1;31m{student["situation"]}\033[m')