from random import randint
from time import sleep
computador = randint(0,10) #faz o computador pensar
print('==xx=='*20)
print('\033[31mvou pensar no numero entre 0 e 10 tente adivinhar')
print('==xx=='*20)
jogador = 0
totjog=0
while jogador != computador:
    jogador = int(input('\033[33mDiga seu palpite :'))
    if jogador < computador :
        print('MAIS...TENTE NOVAMENTE')
        totjog += 1
    else:
        print('MENOS... TENTE NOVAMENTE')
        totjog += 1
    if jogador==computador:
        print('\033[31mVocê acertou, precisou de {} tentativas ,PARABÉNS!!!'.format(totjog))
print('***fim***')