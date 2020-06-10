from datetime import date
ano_atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = ano_atual - nasc

print(f'O atleta possui {idade} anos agora em {ano_atual}.')
if idade <= 9:
    print('Esse atleta é da categoria {}MIRIM{}'.format('\033[4;32m', '\033[m'))
elif 14 >= idade > 9:
    print('Esse atleta é da categoria {}INFANTIL{}'.format('\033[4;32m', '\033[m'))
elif 19 >= idade > 14:
    print('Esse atleta é da categoria {}JÚNIOR{}'.format('\033[4;32m', '\033[m'))
elif 25 >= idade > 19:
    print('Esse atleta é da categoria {}Sênior{}'.format('\033[4;32m', '\033[m'))
elif idade > 25:
    print('Esse atleta é da categoria {}MASTER{}'.format('\033[4;32m', '\033[m'))
print('\nObrigado pela preferência!!!')


