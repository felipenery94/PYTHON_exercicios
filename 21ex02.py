def fatorial(a, show=False):
    """
    ->CALCULA O FATORIAL DE UM NÚMERO
    :param a: NÚMERO A SER CALCULADO
    :param show: INDICA SE QUER MOSTRAR O CALCULO OU NÃO
    :return:RETORNA O VALOR FATORIAL DE UM NÚMERO
    """
    f = 1
    print('--'*10)
    for c in range(a , 0 , -1):
        if show:
            print(f'{c}', end='')
            print(f'x 'if c > 1 else '=', end= '')
        f*=c
        c-=1
    return f

print(fatorial(10, show=True))
help(fatorial)