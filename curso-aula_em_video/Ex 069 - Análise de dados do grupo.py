print('-' * 26)
print('Cadastramento de Pessoas'.center(26))
print('-' * 26)
homem = mais_18 = menos_20f = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = resp = ' '
    while sexo not in 'MfmF':
        sexo = str(input('Informe o sexo:[M/F] ')).strip()[0]
        print('Opção inválida, tente mais uma vez' if sexo not in 'MmfF' else '')
    homem = homem + 1 if sexo in 'mM' else homem
    mais_18 = mais_18 + 1 if idade >= 18 else mais_18
    menos_20f = menos_20f + 1 if sexo in 'fF' and idade < 20 else menos_20f
    while resp not in 'SsnN':
        resp = str(input('Deseja continuar? Sim ou Não? ')).strip()[0]
        print('Opção inválida, tente mais uma vez' if sexo not in 'sSnN' else '')
    if resp in 'Nn':
        break
print('Pessoas com mais de 18 anos: {}\n'
      'Homens cadastrados: {}\n'
      'Mulheres cadastradas menores de 20 anos: {}'.format(mais_18, homem, menos_20f))