from time import sleep
c = ('\033[0;30m',  # 1 sem cores
     '\033[0;30;41m', # 2 vermelho
     '\033[0;30;42m', # 3 verde
     '\033[0;30;43m', # 4 amarelo
     '\033[0;30;44m', # 5 azul
     '\033[0;30;45m', # 6 roxo
     '\033[7;30m',);  # 7 branco

def ajuda(com):
    titulo(f'ACESSANDO O MANUAL DO COMANDO \'{com}\'',4)
    print(c[3], end=' ')
    help(com)
    print(c[3], end='')
    sleep(1)

def titulo(msg ,cor=0):
    tam = len(msg) + 4
    print(c[1], end='')
    print('-'*tam)
    print(f'  {msg}')
    print('-'*tam)
    print(c[1], end='')
    sleep(1)


comando = ' '
while True:
    titulo('SISTEMA DE AJUDA PYHELP')
    comando = str(input('FUNÇÃO OU BIBLIOTECA >>'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO')



