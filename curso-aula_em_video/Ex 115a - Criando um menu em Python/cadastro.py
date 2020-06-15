def menu():
    """
    --> Função que mostra um menu de cadastramento com opções
    :return: sem retorno
    """
    import cor as c
    print('▬' * 48)
    print(f"\t\t\t{c.cores('Sistema de Cadastramento', 'ciano')}")
    print('▬' * 48)
    print(f'{c.cores("1", "blue")} {"•"*21} {c.cores("✎ Cadastrar nova pessoa", "yellow")}\n'
          f'{c.cores("2", "red")} {"•"*21} {c.cores("≣ Listar cadastros", "yellow")}')
    print('▬' * 48)


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
    import cor as c
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


