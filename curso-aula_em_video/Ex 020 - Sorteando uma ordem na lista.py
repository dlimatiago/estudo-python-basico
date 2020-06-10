from random import shuffle
nomes = [
    input('1° nome: '),
    input('2° nome: '),
    input('3° nome: '),
    input('4° nome: ')
]
shuffle(nomes)
print(
    'A ordem de apresentação do trabalho é {}'. format(nomes)
)