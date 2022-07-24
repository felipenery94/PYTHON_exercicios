n = int(input('digite um numero'))
tot = 0
for c in range(1, n +1):
    if n % c == 0:
        print('\033[31m',end= ' ')
        tot +=1
    else:
        print('\033[32m', end=' ')
    print('{}'.format(c), end= ' ')
print('\n\033[0mO número {} , foi divisivel {} vezes'.format(n , tot))
if tot == 2:
    print('Portanto é primo'.format(n))
else:
    print('Portanto não é primo'.format(n))