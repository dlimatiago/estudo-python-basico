from time import sleep
from datetime import date, datetime
import pygame
tdy, clock = date.today(), datetime.now()
print('\033[7;31;1m Loja do Bairro \033[m')  # Nome loja
print('\033[33;1m{}\033[m'.format(tdy.strftime('%d/%m/%Y')), end=' ')  # Dia de hj
print('\033[1;33m{}\033[m'.format(clock.strftime('%H:%M')))  # Que horas iniciou
pygame.mixer.init()
pygame.mixer.music.load('elevador.mp3')
pygame.mixer.music.play()
input('Aperte Enter para iniciar a operação')
spended = plus1000 = cheaper = c = pricecheaper = 0
while True:
    c += 1
    product = str(input('Produto: ')).strip().capitalize()
    price = float(input('Preço do produto: R$'))
    spended += price
    plus1000 = plus1000 + 1 if price >= 1000 else plus1000
    if c == 1 or price < pricecheaper:
        cheaper = product
        pricecheaper = price
    ans = ' '
    while ans not in 'nsNS':
        ans = str(input('Vai continuar? [S/N]')).strip()[0]
        print('Opção inválida' if ans not in 'nNsS' else '')
    if ans in 'nN':
        break
print('\033[33;4;1mEstamos calculando os gastos e reunindo informações úteis\033[m')
sleep(1.3)
print('\033[33;1mAqui estão:\033[m ')
print(f'O seu total gasto na nossa loja foi \033[31;4;1mR${spended:.2f}\033[m\n'
      f'A gente percebeu que seu produto mais barato foi \033[32;1;4m{cheaper}\033[m\n'
      f'Além disso, vimos que tiveram \033[32;4;1m{plus1000}\033[m produtos custando mais de R$1000.00')
print('\n\033[4;1;34mObrigado pela prefência!!! Estamos finalizando a operação\033[m')
sleep(2)
print('\n\033[1;32Obrigado e até a próxima!!!\033[m')
pygame.mixer.music.fadeout(10)
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx FINALIZADO xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')