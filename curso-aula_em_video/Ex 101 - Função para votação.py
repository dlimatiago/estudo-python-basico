def voto(nasc):
    from datetime import date
    ano_a = date.today().year
    idade = ano_a - nasc
    if 18 > idade >= 16 or idade >= 65:
        return f'Você possui {idade} anos: \033[1;34mVoto Opcional\033[m'
    elif 75 > idade >= 18:
        return f'Você possui {idade} anos: \033[1;33mVoto obrigatório\033[m'
    else:
        return f'Você possui {idade} anos: \033[1;31mVoto proibído\033[m'


ano = int(input('Digite ano de nascimento: '))
print(voto(ano))
print('Fim do programa!')