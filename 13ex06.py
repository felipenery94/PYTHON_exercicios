cont = 0
soma = 0
for c in range(1 , 7 ):
    n = int(input('digite um número'))
    if n % 2 == 0:
        cont += 1
        soma += n
print('A soma dos {} números pares é {}'.format(cont , soma))