def cores(texto='', cor='close'):
    """
    --> Adiciona cores a uma string
    :param texto: Valor literal que deseja adicionar cor
    :param cor: a cor que deseja aplicar. São elas:
            red, green, yellow, blue, magenta, ciano
    :return: retorna um valor tipo str com a cor escolhida
    """
    global txt
    color = {'red': '\033[31m',
             'green': '\033[32m',
             'yellow': '\033[33m',
             'blue': '\033[34m',
             'magenta': '\033[35m',
             'ciano': '\033[36m',
             'close': '\033[m'}
    txt = f'{color[cor]}{texto}{color["close"]}'
    return txt
