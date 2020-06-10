def escreva(txt, form, cor, sep, n):
    color = {'red': '\033[31m',
             'gre': '\033[32m',
             'yel': '\033[33m',
             'blu': '\033[34m',
             'non': '\033[m',
             'clo': '\033[m'}
    sprd = {'til': '~', 'tra': '-', 'ast': '*',
            'has': '#', 'igu': '=', 'combo': '-=-'}
    form, n = int(form), int(n)
    if form == 0:
        print(sprd[sep] * n)
        print(f'{color[cor]}{str(txt).center(n)}{color["clo"]}')  # Txt centralizado
        print(sprd[sep] * n)
    elif form == 1:
        print(sprd[sep] * n)
        print(f'{color[cor]}{str(txt).upper().center(n)}{color["clo"]}')
        print(sprd[sep] * n)
    elif form == 2:
        print(sprd[sep] * n)
        print(f'{color[cor]}{str(txt).lower().center(n)}{color["clo"]}')
        print(sprd[sep] * n)
    elif form == 3:
        print(sprd[sep] * n)
        print(f'{color[cor]}{str(txt).title().center(n)}{color["clo"]}')  # Método errado, trocado para title()
        print(sprd[sep] * n)
    else:
        print(f'{color["red"]}ERRO 405. METHOD NOT ALLOWED{color["clo"]}')


print("""Adapte a sua mensagem:
Formatação:
    0   → Sem alteração
    1   → Todas maiúsculas
    2   → Todas minúsculas
    3   → Título de livro
Cor:
    non → Padrão
    red → Vermelho
    gre → Verde
    yel → Amarelo
    blu → Azul
Separador:
    ~   → til
    -   → tra
    *   → ast
    #   → has
    =   → igu
    -=- → combo
""")
escreva(input('Texto: '), input('Formatação: '), input('Cor: '), input('Separador: '), input('Tamanho: '))

