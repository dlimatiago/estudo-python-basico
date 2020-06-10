from time import sleep
for contagem in range(10, -1, -1):
    print(contagem)
    sleep(1)
print('{}FELIZ ANO NOVO !!!!{}'.format('\033[33m', '\033[m'))