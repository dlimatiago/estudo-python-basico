
vel = int(input('\033[1;36mInforme a velocidade do carro:\033[m '))  # Formatado com a cor ciano cod. 36
if vel > 80:
    print('\033[1;31mVocê excedeu o limite de 80 km/h\033[m')  # Formatado com a cor vermelha cod. 31 e negrito
    print(f'Sua multa será de \033[4;33mR${float((vel-80)*7):.2f}\033[m')  # Valor em amarelo cod. 33
print('\033[1;32mVocê está dentro do limite, dirija com cuidado\033[m')  # Cor em verde cod. 32