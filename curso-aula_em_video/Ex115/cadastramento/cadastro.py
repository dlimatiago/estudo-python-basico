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


def cadastrar(nome='', idade=0):
    """
    --> Cadastra o nome e a idade de uma pessoa em um arquivo.
    :param nome: Nome da pessoa que se deseja escrever no arquivo
    :param idade: Idade da pessoa que deseja escrever no arquivo
    :return: Sem retorno
    """
    cadastro = open('cadastrados.txt', 'w')
    pessoa = f'{nome}\t{idade}'
    cadastro.write(pessoa)
    cadastro.close()


def mostrar_cadastros():
    """
    --> Função abre um arquivo e lista os nomes e idade na ordem de cadastramento
    :return: Sem retorno
    """
    from interface import inter as c

    ler = open('cadastrados.txt')
    # Criando o cabeçalho da parte dos cadastrados
    print(c.cores('▄' * 60, 'magenta'))
    print('Lista dos Cadastrados'.center(60))
    print(c.cores('▄' * 60, 'magenta'))
    print(f'{"Nome":<4}{"Idade":>40}')
    print(c.cores('▄' * 60, 'blue'))

    dados = ler.readlines() # Separa os elementos da linha do arquivo em uma lista
    for linha in dados:  # Percorre os elementos na lista
        dados = linha.split()
        for e in dados:
            if e.isalpha():
                print(e)
    ler.close()


