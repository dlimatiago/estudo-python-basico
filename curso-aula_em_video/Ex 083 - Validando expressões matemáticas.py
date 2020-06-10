exp = str(input('Digite qualquer expressão: '))
matches = []
for simbol in exp:
    if simbol == '(':
        matches.append(simbol)
    if simbol == ')':
        if len(matches) > 0:
            matches.pop()  # Remove o último elemento da lista
        else:
            matches.append(simbol)
            break
print('Sua expressão é \033[1;31;4minválida\033[m!' if len(matches) != 0
      else 'Sua expressão é \033[1;32;4mválida\033[m!')
