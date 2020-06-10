
n = int(input('Digite um número inteiro: '))
resposta = int(input(
    'Escolha uma das bases para conversão:\n'
    '[1] Converter para BINÁRIO\n'
    '[2] Converter para OCTAL\n'
    '[3] Converter para HEXADECIMAL\n'
    'Resposta: '
))

if resposta == 1:
    print(f'{n} convertido em BINÁRIO é {bin(n)[2:]}')
elif resposta == 2:
    print(f'{n} convertido em OCTAL é {oct(n)[2:]}')
elif resposta == 3:
    print(f'{n} convertido em HEXADECIMAL é {hex(n)[2:]}')
else:
    print('Opção invalida. Tente novamente')