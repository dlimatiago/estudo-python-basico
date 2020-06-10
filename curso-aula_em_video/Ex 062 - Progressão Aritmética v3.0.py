print('''
  ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ 
 █   {}OS 10 TERMOS DE UMA P.A{}        █ 
  ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬'''.format('\033[31m', '\033[m'))
termo = int(input('1° termo da P.A.: '))
razao = int(input('A razão dessa P.A.: '))
c, pa, qtermos, op = 0, 0, 10, 10
while c <= op != 0:
    pa = pa + termo if c == 0 and qtermos == 10 else pa + razao
    print(pa, end=' → ')
    c += 1
    if c == op:
        print('PAUSA')
        op = int(input('Deseja mostrar mais quantos termos? '))
        qtermos += op
        c = op if op == 0 else 0
print('PA finalizada com {} termos mostrados.'.format(qtermos), end='')