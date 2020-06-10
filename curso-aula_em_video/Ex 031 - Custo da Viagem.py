distancia = float(input('Qual a distância da sua viagem? '))
valor = distancia*.5 if distancia <= 200 else distancia*.45
print(
    'Sua viagem tem um total de \033[4;33m{} Km\033[m.\n'
    'O preço da passagem é \033[4;33mR$ {:.2f}\033[m'.format(distancia, valor)
)
