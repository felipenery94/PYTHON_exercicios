from random import randint
from time import sleep
from random import randint
print('''Suas opçoes:
[0] PEDRA'
[1] PAPEL'
[2] TESOURA''')
itens = ('PEDRA','PAPEL' , 'TESOURA')
jogador = int(input('Qual sua jogada ?'))
print('jo')
sleep(1)
print('ken')
sleep(1)
print('pô!!!')
print('=='*20)
computador = randint(0,2)
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('**'*20)
if computador == 0 : #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('jogador VENCE')
    elif jogador == 2:
        print('computador VENCE')
if computador == 1: # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('computador VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('jogador VENCE')
if computador == 2: # COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('jogador VENCE')
    elif jogador == 1:
        print('computador VENCE')
    elif jogador == 2:
        print('EMPATE')





