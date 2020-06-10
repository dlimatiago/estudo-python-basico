from math import sin, cos, tan, radians
angulo = float(input('Informe o ângulo desejado em graus: '))
ang = radians(angulo)
print('O ângulo de {x}° possui SENO igual a {s:.1f}\n'
      'O ângulo de {x}° possui COSSENO igual a {c:.1f}\n'
      'O ângulo de {x}° possui TANGENTE igual a {t:.1f}'.format(x=angulo, s=sin(ang), c=cos(ang), t=tan(ang)))