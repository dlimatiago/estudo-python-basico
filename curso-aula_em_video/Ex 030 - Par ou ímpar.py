n = int(input('\033[1;35mInforme um número qualquer:\033[m '))  # Cor magenta cod. 35
if n % 2 != 0:
    print('O número {} é \033[1;34mÍMPAR\033[m'.format(n))  # Cor azul cod. 33
else:
    print('O número {} é \033[1;34mPAR\033[m'.format(n))