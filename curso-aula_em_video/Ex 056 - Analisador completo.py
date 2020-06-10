med, velho, vidade, mulher = 0, 'Não há', 0, 0
for p in range(1, 5):
    print('------- Pessoa {} ------- '.format(p))
    nome = str(input('Nome: '.strip())).capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    med += idade  # Faz a soma da idade de todos
    velho = nome if sexo in'mM' and idade >= vidade else velho  # Nome do homem mais velho
    vidade = idade if sexo in 'mM' and idade >= vidade else vidade  # Salva a idade do mais velho
    mulher += 1 if sexo in 'fF' and idade < 20 else 0  # Conta quantas mulheres tem com menos de 20
print('A média de idade do grupo: {} anos.\n'
      'Nome do home mais velho: {}.\n'
      'Mulheres com menos de 20 anos: {}.'.format(med//4, velho, mulher))

