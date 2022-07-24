n = int(input('me diga um número!'))
resultado = n % 2
if resultado==0:
    print('\033[31mnúmero {} é par '.format(n))
else:
    print('\033[32mnúmero {} é ímpar'.format(n))

