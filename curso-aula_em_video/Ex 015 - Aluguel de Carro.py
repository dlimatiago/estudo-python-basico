dia = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodou? '))
pago = (dia * 60) + (km * 0.15)
print('O preço a ser pago é R$ {:.2f}'.format(float(pago)))

