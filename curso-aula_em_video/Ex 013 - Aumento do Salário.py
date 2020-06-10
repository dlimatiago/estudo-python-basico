salario = float(input('Qual o salário atual do funcionário? R$ '))

print(f'Valor do salario R$ {salario}')

salario += (salario*0.15)

print('O salário com 15% de aumento passa a ser R$ {:.2f}'.format(salario))


