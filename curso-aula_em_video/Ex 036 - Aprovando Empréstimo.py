from math import ceil,trunc
print(
    """
            {}BEHABRAS - BANCO DE EMPRÉSTIMO HABITACIONAL DO BRASIL{}
""".format('\033[4;32m', '\033[m')
)
print(
    '''                               {}ATENÇÃO{}
                {}este aplicativo irá ajudar a simular as
                possibilidade de contrair um emprestimo
               habitacional. Preencha os seus dados com
              cuidado e cautela. Agradeçemos a preferência!{}
    '''.format('\033[1;31m', '\033[m', '\033[1;33m', '\033[m')
)
valorCasa = float(input('Informe o valor do {}imóvel{} para financiamento: R$ '.format('\033[4;36m', '\033[m')))
salario = float(input('Informe o valor do {}salário{} do requisitante: R$ '.format('\033[4;32m', '\033[m')))
anos = int(input('Informe quantos a quantidade de {}anos{} do financiamento: '.format('\033[4;33m', '\033[m')))

prestação = valorCasa / (anos * 12)
salario30p = salario * 0.30
if prestação >= salario30p:
    print('{}Seu emprestimo foi negado!!!{}'.upper().format('\033[4;31m', '\033[m'))
    print('A prestação mínima para esse imóvel é de {s}R${w:.2f}{q}'.format(w=prestação, s='\033[33m', q='\033[m'))
    print('Você só pode arcar com uma prestação de {s}R${h:.2f}{q}'.format(h=salario30p, s='\033[33m', q='\033[m'))
else:
    print('{}PARABÉNS, seu empréstimo foi aprovado com sucesso!!!{}'.upper().format('\033[4;32m', '\033[m'))
    print('Valor da parcela mensal: R$ {a:.2f}\nValor do empréstimo aprovado: R$ {d:.2f}'.format(a=prestação,
                                                                            d=trunc(ceil(prestação*anos*12))))
