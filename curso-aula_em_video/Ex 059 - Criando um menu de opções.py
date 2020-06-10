from time import  sleep
valor1 = int(input('Digite o 1° valor: '))
valor2 = int(input('Digite o 2° valor: '))
opção = 0
while opção != 5:
    print("""************************
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
************************""")
    opção = str(input('>>>> Informe a opção desejada: ')).strip()
    if opção in '12345':
        opção = int(opção)
        if opção == 1:
            soma = valor1 + valor2
            print(' {} + {} = {}'.format(valor1, valor2, soma))
        if opção == 2:
            mult = valor1 * valor2
            print('{} x {} = {}'.format(valor1, valor2, mult))
        if opção == 3:
            if valor2 != valor1:
                maior = max((valor1, valor2))
                print('O maior valor entre {} e {} é {}'.format(valor1, valor2, maior))
            else:
                print('Os valores são iguais!')
        if opção == 4:
            valor1 = int(input('Digite o 1° valor: '))
            valor2 = int(input('Digite o 2° valor: '))
        if opção == 5:
            print('Aguarde enquanto finalizamos o programa')
            print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
sleep(3)
print('Obrigado por usar o nosso programa. Volte sempre!')