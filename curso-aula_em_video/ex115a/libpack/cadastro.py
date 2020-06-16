def leiaint(msg):
    while True:
        try:
            integer = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Os dados inseridos são inválidos!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[35mProcesso interrompido pelo usuário\033[m')
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
    cadastro = open('cadastrados.txt', 'a')  # Abrindo o arquivo para colocar o nome e idade
    pessoa = f'{nome}\t{idade}\n'
    cadastro.write(pessoa)
    cadastro.close()


def mostrar_cadastros():
    """
    --> Função abre um arquivo e lista os nomes e idade na ordem de cadastramento
    contido em um dicionario
    :return: Sem retorno
    """
    import visual as v

    ler = open("C:/Users/Tiago/Documents/curso-python/curso-aula_em_video/ex115a/cadastrados.txt")

    pessoa, cad = dict(), list()
    cont, ver = 1, False
    todo, idade = '', ''

    nome = ler.readlines()  # Uma lista formada com o conteudo de cada linha do doc (com \t e \n)
    for i in nome:
        i = i.split()
        # É gerado uma lista com as partes de cada pessoa: Nome sobrenome e idade
        # É verificado para se separar o nome da idade e colocar em um dicionário.
        for n in i:
            if n.isalpha():
                todo += n + ' '
            elif n.isnumeric():
                idade += n
                cont += 1
                ver = True if cont == 2 else False
            if ver is True:
                pessoa['Pessoa'] = todo
                pessoa['Idade'] = idade
                cad.append(pessoa.copy())
                todo, idade = '', ''
                cont, ver = 1, False
    ler.close()


mostrar_cadastros()