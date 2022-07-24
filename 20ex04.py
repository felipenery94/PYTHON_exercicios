from time import sleep
def maior(*valores):
    cont = maior = 0
    print('--'*30)
    print('\nANALISANDO OS VALORES PASSADOS :...')
    for valor in valores:
        print(f'{valor}',end=' ', flush=True)
        sleep(0.4)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f'FORAM INFORMADOS {cont} VALORES AO TODO')
    print(f'O MAIOR VALOR É {maior}')




maior(1,2,35,7)
maior(1,2)
maior(200,100,50)
maior()
maior(15,60,125,-4)

