num = (
    int(input('Digite o 1° número: ')),
    int(input('Digite o 2° número: '))
)
if num[0] > num[1]:
    print('O {}PRIMEIRO{} valor é maior'.format('\033[4;31m', '\033[m'))
elif num[1] > num[0]:
    print('O {}SEGUNDO{} valor é maior'.format('\033[4;31m', '\033[m'))
elif num[0] == num[1]:
    print('Não existe valor maior, os dois são {}IGUAIS{}'.format('\033[4;33m', '\033[m'))