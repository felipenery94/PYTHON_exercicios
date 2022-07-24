print('LOJAS TEM TUDO')
print('***'*20)
total = cont = menor = contm=0
while True :
    produto = str(input('QUAL NOME DO PRODUTO?')).upper().strip()
    preco = float(input('PREÇO DO PRODUTO :'))
    o = ' '
    contm +=1
    while o not in'SN':
        o = str(input('QUER CONTINUAR ? [S/N]')).upper().strip()[0]
        if contm ==1:
            menor = preco
        else:
            if preco < menor:
                menor = preco
    if preco == preco :
        total+=preco
    if preco > 1000:
        cont+=1
    if o == 'N':
        break
print('{:-^40}'.format('COMPRA FINALIZADA'))
print(f'O TOTAL DA COMPRA É DE {total :.2f} REAIS')
print(f'TEMOS {cont} PRODUTOS QUE CUSTAM MAIS DE 1 MIL REAIS')
print(f'O PRODUTO MAIS BARATO É o {menor:.2f}')

