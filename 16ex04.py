n1 = (int(input('DIGITE UM NÚMERO :')),
int(input('OUTRO NÚMERO :')),
int(input('MAIS UM NÚMERO :')),
int(input('ULTIMO NÚMERO :')))
print('**'*20)
print(f'VOCE DIGITOU OS NÚMEROS : {n1}')
if 9 in n1:
    print(f'O NÚMERO 9 APARECE {n1.count(9)} VEZES')
else:
    print('O VALOR 9 NÃO FOI DIGITADO')
if 3 in n1 :
    print(f'O NUMERO 3 ESTÁ NA {n1.index(3)+1}° POSIÇÃO')
else:
    print('O VALOR 3 NÃO FOI DIGITADO')
print(f'OS NÚMEROS PARES DIGITADOS FORAM',end = ' ')
for n in n1:
    if n % 2 == 0 :
        print(n , end = ' ')

