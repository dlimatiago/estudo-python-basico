from calendar import isleap  # isleap informa se é um ano bissexto
from datetime import date  # Ajuda a pegar a data atual do sistema a
ano = int(input('Informe o ano que gostaria de consultar\n'
                'Digite \033[4;33m0\033[m caso queira o ano corrente: '))
if ano == 0:
    ano = date.today().year
teste = 'é BISSEXTO' if isleap(ano) is True else'não é BISSEXTO'
print('O ano de {} {}.'.format(ano, teste))