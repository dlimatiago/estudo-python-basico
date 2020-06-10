numero = float(input('Digite um número: '))

print('O dobro de {a} é {b}.\nO seu triplo é {c}.\nSua raíz quadrada é {d:.2f}.'.
      format(a=numero, b=(2*numero), c=(3*numero), d=(numero**0.5)))
