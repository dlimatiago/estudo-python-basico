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
