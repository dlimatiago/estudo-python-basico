def aumentar(value=0, por=0):
    value *= ((por+100)/100)
    return value


def diminuir(value=0, por=0):
    value *= ((100 - por) / 100)
    return value


def dobro(value=0):
    op = value * 2
    return op


def metade(value=0):
    op = value / 2
    return op


def moeda(value=0):
    global converted
    global integer
    global decimal

    coin, count = str(value), 0
    if '.' in coin:
        coin = coin.replace('.', ',')

    for num in coin:
        if num.isnumeric():
            count += 1
        else:
            break
    if ',' in coin:
        integer, decimal = coin.split(',')
    else:
        integer, decimal = coin, '00'

    if count > 3:
        integer = list(integer)
        i = len(integer)
        for it in range(i, -1, -3):
            if it < i:
                if it != 0:
                    integer.insert(it, '.')
        change = ''
        for item in integer:
            change += item
        integer = change
        if len(decimal) > 2:
            decimal = float(decimal) /10 ** len(decimal)
            decimal = round(decimal, 2)
            decimal = str(decimal).split('.')
            decimal = decimal[1]
        elif len(decimal) == 1:
            decimal += '0'
    else:
        if len(decimal) > 2:
            decimal = float(decimal) / 10 ** len(decimal)
            decimal = round(decimal, 2)
            decimal = str(decimal).split('.')
            decimal = decimal[1]
        elif len(decimal) == 1:
            decimal += '0'

    converted = 'R$ ' + integer + ',' + decimal
    return converted
