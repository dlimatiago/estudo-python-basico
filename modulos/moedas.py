def aumentar(value=0, por=0, formatting=True):
    value *= ((por+100)/100)
    if formatting is True:
        value = moeda(value)
    return value


def diminuir(value=0, por=0, formatting=True):
    value *= ((100 - por) / 100)
    if formatting is True:
        value = moeda(value)
    return value


def dobro(value=0, formatting=True):
    op = value * 2
    if formatting is True:
        op = moeda(op)
    return op


def metade(value=0, formatting=True):
    op = value / 2
    if formatting is True:
        op = moeda(op)
    return op


def moeda(value=0, cifra='R$'):
    global converted
    global integer
    global decimal

    coin = str(value)
    if '.' in coin:
        integer, decimal = coin.split('.')
    else:
        integer, decimal = coin, '00'
# Formatando a parte inteira
    integer = list(integer)
    for i in range(len(integer), -1, -3):
        integer.insert(i, '.') if i < len(integer) and i != 0 else '-'
    transition = ''
    for item in integer:
        transition += item
    integer = transition
# Formatando a parte decimal
    if len(decimal) > 2:
        decimal = round(float(decimal) / 10 ** len(decimal), 2)
        decimal = str(decimal)[2:]
    elif len(decimal) == 1:
        decimal += '0'
# Juntando as partes formatadas
    converted = cifra + integer + ',' + decimal
    return converted
