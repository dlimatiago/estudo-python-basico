soma = c = 0
while True:
    n = int(input('Digite um número (999 para sair): '))
    if n == 999:
        break
    c += n
    soma += 1
print(f'Foram lidos {c} números e a soma deles é {soma}.')