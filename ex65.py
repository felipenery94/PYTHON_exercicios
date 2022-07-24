a = []
b = []
c = []
while True:
    n = (int(input(f'DIGITE UM NÚMERO : ')))
    a.append(n)
    resp = str(input('QUER CONTINUAR S/N ? '))
    if n % 2 == 0:
        b.append(n)
    else:
        c.append(n)
    if resp in 'Nn':
        break
print(f'TOTAL DE NÚMEROS DIGITADOS : {a}')
print(f'NÚMEROS PARES DIGITADOS : {b}')
print(f'NÚMEROS IMPARES DIGITADOS : {c}')

