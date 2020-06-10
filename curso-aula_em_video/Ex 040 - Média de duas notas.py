from statistics import mean
notas = (float(input('Digite a 1° nota: ')),
         float(input('Digite a 2° nota: ')))
med = mean(notas)
if med < 5:
    print('Você foi {}REPROVADO{}'.format('\033[1;31m', '\033[m'))
    print(f'Sua média final foi {med:.1f}')
elif 7 < med <= 5:
    print('Você está de {}RECUPERAÇÃO{}'.format('\033[1;33m', '\033[m'))
    print(f'Sua média foi de {med:.1f}')
elif med >= 7:
    print('Você foi {}APROVADO{}'. format('\033[1;34m', '\033[m'))
    print(f'Sua média foi de {med:.1f}')