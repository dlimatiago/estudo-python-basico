from modulos import moedas as m

money = float(input('Digite um valor: R$ '))
pctg = float(input('Digite uma porcentagem: '))

form = m.moeda(money)
rise = m.aumentar(money, pctg)
down = m.diminuir(money, pctg)
d = m.dobro(money)
met = m.metade(money)

print('-=-' * 30)
print(f'Você informou o valor de {form} e:')
print(f'    Com aumento de {pctg}%, {form} passa a valer {rise}')
print(f'    Com a subtração de {pctg}%, {form} passa a valer {down}')
print(f'    Temos também que o dobro de {form} é {d}')
print(f'    E sua metade é {met}')

