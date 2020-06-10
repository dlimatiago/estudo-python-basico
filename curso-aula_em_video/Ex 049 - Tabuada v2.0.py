tab = int(input('Qual tabuada gostaria de ver? '))
for m in range(1, 11):
    print('{} x {:2} = {}'.format(tab, m, tab*m))