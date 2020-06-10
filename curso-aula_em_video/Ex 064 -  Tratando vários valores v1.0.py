soma, cont = 0, 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Foram mostrados {}{}{} números e '
      'a soma deles é {}{}{}.'.format('\033[33;4m', cont, '\033[m', '\033[34;4m', soma, '\033[m'))