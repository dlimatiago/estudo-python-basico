salario = float(input('Informe o salário do funcionário: R$'))
novo = (salario + (salario * 0.1)) if salario > 1250 else (salario + (salario * 0.15))
print('O salário de \033[4;31mR${:.2f}\033[m passa a ser \033[4;32mR${:.2f}\033[m'.format(salario, novo))