import libpack.visual as v
import libpack.cadastro as cd

opc = v.menu(("✎ Cadastrar nova pessoa", "≣ Listar cadastros", "☓ Sair do sistema"), 'blue', 'yellow')
while True:
    if str(opc) in '123':
        break
    print(f'{v.cores("Essa opção não existe, digite novamente!", "yellow")}')
    opc = cd.leiaint('Digite a opção >>> ')

if opc == 1:
    nome = str(input('► Nome e sobrenome: ')).strip().title()
    idade = cd.leiaint('► Idade: ')
    teste = nome.split()
    # Para controle, apenas 3 a 4 sobrenomes. Esse if faz essa seleção desses nomes
    # Para evitar que nomes como da Silva fique só com o da, ele adiciona o nome seguinte.
    if len(teste) > 3:
        if teste[2].lower() in 'da de di do das dos e':
            nome = teste[0]+' '+teste[1]+' '+teste[2]+' '+teste[3]
        else:
            nome = teste[0] + ' ' + teste[1] + ' ' + teste[2]

    cd.cadastrar(nome, idade)

# if opc == 2:


