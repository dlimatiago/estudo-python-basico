n = str(input('Digite seu nome: ')).lower().strip()
n = n.split()
print(
    'Muito prazer em te conhecer!!\n'
    'Seu primeiro nome é {}\n'
    'Seu último nome é {} '.format(n[0].capitalize(), n[len(n)-1].capitalize())
)
