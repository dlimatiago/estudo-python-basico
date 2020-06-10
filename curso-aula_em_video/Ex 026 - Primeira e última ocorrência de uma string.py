frase = str(input('Digite uma frase: ')).strip().lower()
print(
    'A letra A aparece {} vezes\n'
    'Ela aparece primeiro na posição {}\n'
    'Ela aparece por último na posição {}'.format
    (frase.count('a'), frase.find('a'), frase.rfind('a'))
)