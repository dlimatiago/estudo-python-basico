numlist = []
sit = 0
color = ('\033[1;4;31m', '\033[1;4;32m', '\033[1;4;33m', '\033[1;4;34m',
       '\033[1;4;35m', '\033[36;1;4m', '\033[1;4;37m', '\033[m')
for number in range(5):
    n = int(input('Digite um número: '))
    if number == 0:
        numlist.append(n)
        print(f'O número {color[1]}{n}{color[7]} foi adicionado na {color[2]}última posição{color[7]}!')
    elif number > 0:
        for pos, item in enumerate(numlist):
            if n > item:
                verify = True
            elif n < item:
                sit = pos if numlist[sit] <= item and pos <= sit or item > n > numlist[sit] else sit
                verify = False
        if verify is True:
            numlist.append(n)
            print(f'{color[5]}{n}{color[7]} colocado na {color[6]}última posição{color[7]}!')
        if verify is False:
            numlist.insert(sit, n)
            print(f'{color[3]}{n}{color[7]} colocado na posição {color[4]}{sit}{color[7]}!')
print(f'A lista ordenada com os número dados: {numlist}')
