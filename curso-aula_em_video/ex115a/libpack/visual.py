def titulo(t='', c='close', tam=48):
    """
    --> Função que cria um cabeçalho
    :param t: Texto para fazer o cabeçalho
    :param c: Cor para dar ao texto do cabeçalho.
        cores: red, green, yellow, blue, magenta, close(default)
    :param tam: Tamanho das linhas do cabeçalho
    :return: sem retorno
    """
    print('▬' * tam)
    print(f"{cores(t, c).center(tam)}")
    print('▬' * tam)


def menu(opções, coropc='close', cortxt='close'):
    """
    --> Função que cria um menu de opções.
    :param opções: São as opções que deseja se colocar no menu, tipo tuple.
    :param coropc: Cor desejada para dar as opções.
    :param cortxt: Cor desejada para dar ao texto das opções.
    Cores disponíveis:  - red, green, yellow, blue, magenta, ciano, close(default)
    :return: Retorna o valor escolhido informado no menu.
    """
    import libpack.cadastro as cd

    titulo('Sistema de Cadastramento', 'red')
    for i, o in enumerate(opções):
        print(f'{cores(str(i+1), coropc)} {"•"*21} {cores(o, cortxt)}')

    print('▬' * 48)
    resp = cd.leiaint('Digite a opção >>> ')
    return resp


def cores(texto='', cor='close'):
    """
    --> Adiciona cores a uma string
    :param texto: Valor literal que deseja adicionar cor
    :param cor: a cor que deseja aplicar. São elas:
            red, green, yellow, blue, magenta, ciano, close(default)
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


def tabela(lista, ind, tit='Tabela', cor_t='close', d=10):
    """
    --> Função que cria uma tabela dado um lista ( com dicionários ou listas dentro),
    o título e a cor
    :param lista: Lista passada contendo os valores
    :param ind: Indices da tabela passados em forma de tuple.
    :param tit: Titulo da tabela
    :param cor_t: Cor do título da tabela
    Cores: red, green, yellow, blue, magenta, ciano, close(default)
    :param d: Distancia entre os itens da tabela
    :return: Sem retorno
    """
    #  Essa geradora  converte para lista o item dentro da lista, caso seja um dict, set ou tuple
    valores = [list(i.values()) if type(i) is dict else i for i in lista]
    indices = ind

    titulo(tit, cor_t)
    for i in indices:
        print(f'{i:6}', end='\t\t\t\t\t')
    print()
    for val in valores:
        print(f'{val[0]:6} {"•"*d} {val[1]:3} anos')


