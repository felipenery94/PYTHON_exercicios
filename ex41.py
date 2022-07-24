n1 = int(input('Digite um valor :'))
n2 = int(input('Digite segundo valor :'))
opcao = 0
while opcao != 5:
    print('''
        [1] somar :
        [2] multiplicar:
        [3] maior:
        [4] digite novos números:
        [5] sair do programa: ''')
    opcao = int(input('Escolha opcao desejada :'))
    if opcao == 1:
        somar = n1 + n2
        print('A soma de {} + {} é = {}'.format(n1 ,  n2 , somar))
    elif opcao == 2 :
        mult = n1*n2
        print('A multiplicação de {} x {} = {}'.format(n1,n2,mult))
    elif opcao ==3:
        if n1 > n2 :
            print('O maior número é {}'.format(n1))
        else:
            print('O maior número é {}'.format(n2))
    if opcao == 4:
        print('Digite novamente !')
        n1 = int(input('Digite um valor :'))
        n2 = int(input('Digite segundo valor :'))
if opcao == 5:
    print('VOÇÊ SAIU DO PROGRAMA! OBRIGADO POR UTILIZAR!')




