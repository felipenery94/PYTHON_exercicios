def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError , TypeError):
            print('\033[31mERRO!! DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mprograma de dados interrompido pelo usúário\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError , TypeError):
            print('\033[31mERRO!! DIGITE UM NÚMERO REAL VÁLIDO\033[31m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mERRO!! PROGRAMA INTERROMPIDO PELO USUÁRIO\033[31m')
            return 0
        else:
            return n

n1 = leiaint('digite um númeri inteiro :')
n2 = leiafloat('digite um número real:')
print(f'\033[33mO NÚMERO INTEIRO FOI {n1} E O NÚMERO REAL FOI {n2}\033[33m')






