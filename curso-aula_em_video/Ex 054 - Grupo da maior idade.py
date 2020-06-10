from datetime import date
maior, menor = 0, 7
for i in range(1, 8):
    nasc = int(input('Ano de nascimento da {}° pessoa: '.format(i)))
    maior += 1 if (date.today().year - nasc) >= 18 else 0
print('Menores de idade: {}\nMaiores de idade: {}'.format(menor-maior, maior))