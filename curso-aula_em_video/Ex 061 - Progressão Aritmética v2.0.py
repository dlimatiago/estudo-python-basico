print('''
  ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ 
 █   {}OS 10 PRIMEIROS TERMOS DE UMA P.A{}   █ 
  ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬'''.format('\033[31m', '\033[m'))
termo = int(input('1° termo da P.A.: '))
razao = int(input('A razão dessa P.A.: '))
c, pa = 1, 0
while c < 11:
    pa = pa + termo if c == 1 else pa + razao
    print(pa, end=' → ')
    c += 1
print('FIM')