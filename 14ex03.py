#from math import factorial
#n= int(input('digite um número :'))
#print('fatorial do número {} é {}'.format(n,factorial(n)))
'''n = int(input('digite um número para calcular sua fatorial :'))
c = n
f = 1
print('CALCULANDO {}!='.format(n), end = '')
while c > 0 :
    print('{}'.format(c), end = '')
    print('x' if c > 1 else '=', end = '')
    f*=c
    c-=1
print('{}'.format(f))'''
n = int(input('Digite um número para calcular fatorial:'))
c = n
f =1
print('calculando {}!='.format(n),end = '')
for c in range(n,0,-1):
    print('{}'.format(c), end ='')
    print('x' if c > 1 else'=' ,end ='')
    f*=c
    c -=1
print('{}'.format(f))
