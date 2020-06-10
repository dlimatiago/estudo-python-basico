vowels = ('a', 'e', 'i', 'o', 'u')
words = ('item', 'gratuito', 'proibido', 'rubrica', 'pudico', 'menu', 'ali', 'raiz', 'higiene', 'europeia')
print('Vogais ausentes: ', '\033[31m-\033[m')
for w in words:
    print(f'A palavra \033[1;34m{w.upper():^10}\033[m tem:', end=' ')
    for v in vowels:
        print(f'\033[33m{v}\033[m' if v in w else f'\033[31m{"-"}\033[m', end=' ')
    print()
