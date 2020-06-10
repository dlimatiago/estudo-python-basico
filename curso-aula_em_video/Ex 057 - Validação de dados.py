cond = False
while cond is False:
    sexo = str(input('Informe o seu sexo: [M/F]')).strip().upper()[0]
    if sexo in 'MF':
        cond = True
        print('{}Sexo {} registrado com sucesso!!!{}'.format('\033[34;4m', sexo, '\033[m'))
    else:
        print('Dados inválidos. Por favor, repita a operação.')