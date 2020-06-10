resp, maior, media, contador, menor = 's', 0, 0, 0, 0
while resp in 'Ss':
    n = int(input('Digite um valor: '))
    contador += 1
    maior = n if contador == 1 or n > maior else maior
    menor = n if contador == 1 or n < menor else menor
    media += n
    resp = str(input('Deseja continuar? [S/N] ')).strip()[0]
print('Quantidade de números lidos: {}\n'
      'Maior número lido: {}\n'
      'Menor número lido: {}\n'
      'Média dos números lidos: {:.1f}'.format(contador, maior, menor, media/contador))