from time import sleep


def contador(i , f , p):
    if p < 0:
        p*=-1
    if p ==0:
        p = 1
    print('--'*20)
    print(f'CONTAGEM DE {i} ATÉ {f} DE {p} EM {p}')
    sleep(2)
    if i < f:
        cont = i
        while cont <= f:
            print(f' {cont}',end= ' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            cont -= p
            sleep(0.5)
        print('FIM')
contador(1 , 10 ,1)
contador(10 , 0 , 2)
print('AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM !!')
ini = int(input('INICIO :'))
fim = int(input('FIM   :'))
pas = int(input('PASSO :'))
contador(ini, fim , pas)-

