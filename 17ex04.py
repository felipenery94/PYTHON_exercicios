lista = []
c = 0
while True:
    n = int(input('DIGITE UM VALOR ?'))
    lista.append(n)
    c +=1
    r  = str(input('QUER CONTINUAR ? S/N'))
    if r in 'Nn':
        break
print('-='*30)
if 5 not in lista:
    print('NÚMERO 5 NÃO FOI ENCONTRADO NA LISTA')
else:
    print('NÚMERO 5 ESTÁ NA LISTA')
lista.sort(reverse=True)
print(f'LISTA EM ORDEM DECRESCENTE{lista}')
print(f'FORAM DIGITADOS {c} ELEMENTOS')
