nome = input('Digite seu nome completo: ').strip()
p_nome = nome.split()
t_nome = len(p_nome[0])
print(
    'Analisando seu nome...\n'
    'Seu nome em maiúsculas é {M}\n'
    'Seu nome em minúsculas é {m}\n'
    'Seu nome tem ao todo {i} letras\n'
    'Seu primeiro nome é {n} e tem {q} letras'.format(M=nome.upper(), m=nome.lower(),
                                                      i=len(nome) - nome.count(' '), n=p_nome[0].capitalize(), q=t_nome)
)