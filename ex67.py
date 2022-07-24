galera = []
temp= []
pesomai = pesomen = 0
while True :
    temp.append(str(input('NOME : ')))
    temp.append(float(input('PESO : ')))
    if len(galera) == 0 :
        pesomai = pesomen = temp[1]
    else:
        if temp[1] > pesomai:
            pesomai = temp[1]
        if temp[1] < pesomen:
            pesomen = temp[1]
    galera.append(temp[:])
    temp.clear()
    resp = str(input('QUER CONTINUAR [S/N]'))
    if resp in 'Nn':
        break
print(f'TOTAL DE {len(galera)} PESSOAS CADASTRADAS')
print(f'A PESSOA MAIS PESADA É {pesomai}kg PESO DE ',end = ' ')
for p in galera :
    if p[1] == pesomai:
        print(f'[{p[0]}]', end = ' ')
print()
print(f'A PESSOA MAIS LEVE É {pesomen} kg',end = ' ')
for p in galera :
    if p[1]==pesomen:
        print(f'[{p[0]}]',end=' ')
print()