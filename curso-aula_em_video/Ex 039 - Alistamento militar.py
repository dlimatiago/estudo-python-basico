from datetime import date
print(
    """Informe o seu gênero
[1] Masculino
[2] Feminino"""
)
opcao = int(input())
if opcao == 1:
    ano = int(input('Informe o ano de seu nascimento: '))
    idade = int(date.today().year) - ano
    saldo = idade - 18
    anoAtual = date.today().year
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, anoAtual))
    if idade < 18:
        print('Você ainda vai se alistar. Falta {} anos.'.format(-saldo))
        print('Seu alistamento será em {}'.format(ano+18))
    elif idade > 18:
        print('Já passou do tempo de alistamento. Deveria ter se alistado há {} anos'.format(saldo))
        print('Seu alistamento foi em {}'.format(ano+18))
    else:
        print('Hora de se alistar {}IMEDIATAMENTE{}'.format('\033[31m', '\033[m'))
elif opcao == 2:
    print('Você não precisa se alistar nas forças armadas')
else:
    print('Opção inválida')
print('-'*25, 'Fim', '-'*25)
