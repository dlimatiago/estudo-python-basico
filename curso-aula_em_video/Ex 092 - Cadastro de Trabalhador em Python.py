from datetime import datetime

ano_atual = datetime.today().year  # Pega o ano atual

worker = dict()  # Dicionário com as informações do trabalhador
worker['Nome'] = str(input('Nome do trabalhador: ')).strip().title()
nasc = int(input('Ano de nascimento: '))
worker['Idade'] = ano_atual - nasc
num = int(input('CTPS (Caso não tenha, digite 0): '))

if num != 0:
    worker['Contratação'] = int(input('Ano de contratação: '))
    worker['Salário'] = round(float(input('Salário: R$ ')), 2)  # Arrendoda para 2 casas decimais
    worker['Aposentadoria'] = worker['Contratação'] + 35 - nasc
else:
    worker['CTPS'] = 0
print('-=-' * 15)

for k, i in worker.items():
    print(f'{k}: ', f'R$ {i:.2f}' if k == 'Salário'
    else f'{i} anos' if k == 'Idade' or k == 'Aposentadoria' else i)
