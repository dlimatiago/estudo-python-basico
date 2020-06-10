print('-=-' * 10)
print('{}{:^30}{}'.format('\033[7;1;33m', 'Caixa Eletônico', '\033[m'))
print('-=-' * 10)
cash = int(input('Informe o valor a ser sacado: R$'))
fifbill, twebill, tenbill, onebill, totbills, control = 50, 20, 10, 1, cash, True
cfif = ctwe = cten = cone = 0
while True:
    if totbills % fifbill == 0 and totbills != 0 and control is True:
        cfif += 1
        totbills -= fifbill
    elif totbills % twebill == 0 and totbills != 0:
        ctwe += 1
        totbills -= twebill
    elif totbills % tenbill == 0 and totbills != 0:
        cten += 1
        totbills -= tenbill
    elif totbills % onebill == 0 and totbills != 0:
        cone += 1
        totbills -= onebill
    else:
        print('-=-' * 10)
        print('O valor requisitado será sacado em:')
        if cfif > 0:
            print(f'\033[1;31m{cfif} notas de R$50\033[m')
        if ctwe > 0:
            print(f'\033[1;33m{ctwe} notas de R$20\033[m')
        if cten > 0:
            print(f'\033[1;35m{cten} notas de R$10\033[m')
        if cone > 0:
            print(f'\033[1;32m{cone} notas de R$1\033[m')
        break
print('Obrigado pela preferência')