cont = totalh = totalm = 0
while True:
    print('CADASTRE UMA PESSOA')
    print('---' * 20)
    i = int(input('IDADE :'))
    print('***'*20)
    s=' '
    o = 's '
    nao = 'n'
    print('***'*20)
    while s not in 'mMfF':
        s = str(input('SEXO: [M/F]')).strip().upper()[0]
    o = str(input('QUER CONTINUAR ? [S/N]')).strip().upper()[0]
    if i >18:
        cont+=1
    if s == 'M':
        totalh+=1
    if s == 'F'and i < 20:
        totalm+=1
    if o == 'N' :
        break
print(f'TEMOS {cont} , maiores de 18 anos')
print(f'TEMOS UM TOTAL DE {totalh} HOMENS CADASTRADOS')
print(f'TOTAL DE {totalm} MULHER COM MENOS DE 20 ANOS ')
