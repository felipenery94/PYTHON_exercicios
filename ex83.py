from random import randint
from time import sleep
def sorteia(lista):
    print('SORTEANDO 5 VALORES DA LISTA ', end='')
    for c in range(0,5):
        n = randint(0,10)
        lista.append(n)
        print(f'{n}', end=' ',flush=True)
        sleep(0.3)
    print('PRONTO')


def pares(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'SOMANDO OS VALORES PARES {lista}, TEMOS {soma}')


num = list()
sorteia(num)
pares(num)