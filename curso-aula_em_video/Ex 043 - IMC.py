peso = float(input('Qual o seu peso? (kg) '))
alt = float(input('Qual a sua altura? (m) '))
imc = peso / alt**2
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO ideal.')
elif 25 > imc >= 18.5:
    print('Você está no PESO IDEAL.')
elif 30 > imc >= 25:
    print('Você está com SOBREPESO.')
elif 40 > imc >= 30:
    print('Você está com OBESIDADE.')
else:
    print('Você está com OBESIDADE MÓRBIDA, tenha cuidado!')