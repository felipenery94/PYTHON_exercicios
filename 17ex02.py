numeros = []
while True:
    n = int(input('DIGITE UM VALOR :'))
    if n not in numeros:
        numeros.append(n)
        print('VALOR ADICIONADO COM SUCESSO')
    else:
        print('NUMERO DUPLICADO, NÃO SERÁ ADICIONADO')
    r = str(input('QUER CONTINUAR ? [S/N]'))
    if r in 'nN':
        break
print('-='*30)
numeros.sort()
print(f'OS NÚMEROS DIGITADOS FORAM {numeros}')
