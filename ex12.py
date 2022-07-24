from random import randint
from time import sleep
computador = randint(0,5) #faz o computador pensar
print('==xx=='*20)
print('\033[31mvou pensar no numero entre 0 e 5 tente adivinhar')
print('==xx=='*20)
jogador = int(input('\033[33mem que número eu pensei?'))#jogador tenta adivinhar
print('\033[4;35mPROCESSANDO....')
sleep(3)
if jogador==computador:
    print('você ganhou')
else:
    print('voce perdeu eu pensei no numero {} e nao no {}'.format(computador,jogador))
    print('***fim***')