from time import sleep
while True:
    tab = int(input('Informe a tabuada para vê-la: '))
    if tab < 0:
        break
    print('-'*10)
    for x in range(1, 11):
        print(f'{tab} x {x:2} = {x*tab}')
    print('-' * 10)
print('encerrando...'.upper())
sleep(1.3)
print('finalizado'.capitalize())