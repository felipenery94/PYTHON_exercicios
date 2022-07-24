soma = cont = total =0
from random import randint
print('JOGO PAR OU IMPAR')
print('**'*20)
while True:
    jogador = int(input('diga um valor :'))
    computador = randint(0 , 10)
    total = jogador + computador
    op=' '
    while op not in 'PI':
        op = str(input('PAR / ÍMPAR')).strip().upper()[0]
    print(f'VOCE JOGOU {jogador} e o computador jogou {computador} total de {total}' , end = ' ')
    print('DEU PAR' if total % 2 ==0 else 'DEU IMPAR')
    if op == 'P':
        if total % 2 == 0:
            print('VOCÊ GANHOU')
            cont+=1
        else:
            print('VOCÊ PERDEU')
            break
    if op == 'I':
        if total % 2 == 1:
            print('VOCÊ GANHOU')
            cont+=1
        else:
            print('VOCÊ PERDEU')
            break
print(f'JOGADOR GANHOU {cont} VEZES!!')
print('JOGUE NOVAMENTE!')






