import math
n = int(input('digite um numero inteiro'))
print('qual base deseja converter:'
'\n [1] converter para binario'
'\n [2] converter para octal'
'\n [3] converter para hexadecimal'
'\n digite o número correspondente a opção')
base = int(input('sua opção'))
if base == 1:
    print('o número inteiro {} , convertido para binário é {}'.format(n , bin(n)[2:]))
elif base == 2:
    print('{} convertido para octal é {}'.format(n, oct(n)[2:]))

elif base == 3:
    print('{} convertido para hexadecimal é {} '.format(n , hex(n)[2:]))
else:
    print('opção invalida')
