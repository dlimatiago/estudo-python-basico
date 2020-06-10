frase = str(input('Digite uma frase: ')).strip().lower()

pontuação = (',', ' ', '-', '.', '!', '?', '"', ':')
acentuação = ('á', 'à', 'â', 'ã', 'é', 'ê', 'í', 'ó', 'ô', 'õ', 'ú')

for x in range(len(pontuação)):
    verificar = pontuação[x] in frase
    if verificar is True:
        frase = frase.replace(pontuação[x], '')
for y in range(len(acentuação)):
    verificar = acentuação[y] in frase
    if verificar is True:
        if 4 > y >= 0:
            frase = frase.replace(acentuação[y], 'a')
        elif 6 > y >= 4:
            frase = frase.replace(acentuação[y], 'e')
        elif y == 6:
            frase = frase.replace(acentuação[y], 'i')
        elif 10 > y >= 7:
            frase = frase.replace(acentuação[y], 'o')
        elif y == 10:
            frase = frase.replace(acentuação[y], 'u')

reverso = frase[::-1].upper()
frase = frase.upper()
if frase == reverso:
    print('O inverso de {} é {} e por isso ela é um PALÍNDROMO!!!'.format(frase, reverso))
else:
    print('O inverso de {} é {} e por isso ela não é um PALÍNDROMO!!!'.format(frase, reverso))
