import cadastro as cd
import cor as c

cd.menu()
while True:
    try:
        opc = int(input('Digite a opção >>> '))
    except (TypeError, ValueError):
        print(f'{c.cores("Erro! Tipo de dados inválidos, digite novamente!", "red")}')
    except KeyboardInterrupt:
        print(f'{c.cores("Processo interrompido pelo usuário", "magenta")}')
        opc = None
        break
    else:
        if str(opc) in '12':
            break
        print(f'{c.cores("Essa opção não existe, digite novamente!", "yellow")}  ')
if opc == 1:
    nome = str(input('► Nome e sobrenome: ')).strip().title()
    idade = cd.leiaint('► Idade: ')
    teste = nome.split()
    if len(teste) > 3:
        if teste[2].lower() in 'da de di do das dos':
            nome = teste[0]+' '+teste[1]+' '+teste[2]+' '+teste[3]
        else:
            nome = teste[0] + ' ' + teste[1] + ' ' + teste[2]

    cd.cadastrar(nome, idade)

# if opc == 2:


