print('''
  ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ 
 █   {}OS 10 PRIMEIROS TERMOS DE UMA P.A{}   █ 
  ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬'''.format('\033[31m', '\033[m'))
termo = int(input('1° termo da P.A.: '))
razao = int(input('A razão dessa P.A.: '))
dec = termo + (10 - 1) * razao
for pa in range(termo, dec + razao, razao):
    print(pa, end=' → ')
print('fim')