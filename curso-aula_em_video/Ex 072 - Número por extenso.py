while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 20 >= n >= 0:
        break
    else:
        print('\033[1;4;31mEssa opção é invalida, digite novamente!!\033[m')
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(f'Você digitou o número {extenso[n]}.')