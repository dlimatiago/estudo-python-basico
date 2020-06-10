print('\033[31m*\033[m'*40)
print('  {}TERMINAL DE PAGAMENTO DA IMAGINARIUM{}'.format('\033[33m', '\033[m'))
print('\033[31m*\033[m'*40)
valor = float(input('Informe o valor que foi gastado aqui na loja: R$'))
print('''Digite o seu método de pagamento escolhido
[1] À vista no Dinheiro ou Cheque
[2] À vista no Cartão de Crédito ou Débito
[3] 2x no Cartão de Crédito
[4] 3x ou mais no Cartão de Crédito
''')
op = int(input('Digite a opção: '))
if op == 1:
    desconto = (valor * 0.1)
    pagar = valor - desconto
    print('''Selecionada essa forma de pagamento, você obteve um \033[4mdesconto de 10%\033[m.
    \033[35mValor da compra\033[m   \033[33mR${:.2f}\033[m
    \033[35mValor do desconto\033[m \033[32mR${:.2f}\033[m
    \033[35mValor a pagar\033[m     \033[37mR${:.2f}\033[m'''.format(valor, desconto, pagar))
elif op == 2:  # Cores: Compra - amarelo, Desconto - verde, Juros - vermelho, pagamento - cinza
    desconto = (valor * 0.05)
    pagar = valor - desconto
    print('''Selecionada essa forma de pagamento, você obteve um \033[4mdesconto de 5%\033[m.
       \033[35mValor da compra\033[m   \033[33mR${:.2f}\033[m
       \033[35mValor do desconto\033[m \033[32mR${:.2f}\033[m
       \033[35mValor a pagar\033[m     \033[37mR${:.2f}\033[m'''.format(valor, desconto, pagar))
elif op == 3:
    pagar = valor
    desconto = 0
    print('''Selecionada essa forma de pagamento...
       \033[35mValor da compra\033[m   \033[33mR${:.2f}\033[m
       \033[35mValor do desconto\033[m \033[32mR${:.2f}\033[m
       \033[35mValor a pagar\033[m     \033[37mR${:.2f}\033[m'''.format(valor, desconto, pagar))
elif op == 4:
    parcelas = int(input('Você pagará em quantas vezes? '))
    juros = (valor * 0.2)
    total = valor + juros
    parc = total / parcelas
    print('''Selecionada essa forma de pagamento, você terá \033[4mjuros total de 20%\033[m.
       \033[35mValor da compra\033[m         \033[33mR${:.2f}\033[m
       \033[35mValor do juros\033[m          \033[32mR${:.2f}\033[m
       \033[35mValor a pagar\033[m           \033[37mR${:.2f}\033[m
       \033[35mValor da parcela mensal\033[m \033[34mR${:.2f}\033[m '''.format(valor, juros, total, parc))
else:
    print('{}OPÇÃO INVÁLIDA DE PAGAMENTO{}'.format('\033[31m', '\033[m'))
    print('Valor a pagar R${:.2f}'.format(valor))