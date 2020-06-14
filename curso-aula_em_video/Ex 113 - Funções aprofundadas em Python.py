def leiaint(msg):
    while True:
        try:
            integer = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Os dados inseridos são inválidos!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[33mO usuário interrompeu o processo\033[m')
            break
        else:
            return integer


def leiafloat(msg):
    while True:
        try:
            flt = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Os dados inseridos são inválidos!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[33mO usuário preferiu não informar dados\033[m')
            break
        else:
            return flt


i = leiaint('Digite um valor inteiro: ')
f = leiafloat('Digite um valor real: ')

print(f'Você digitou {i} como valor inteiro e {f:.2f} para valor real.')
