def area(larg , comp):
    a = larg * comp
    print(f'O TAMANHO DO TERRENO {larg} x {comp} = {a} m²')


print('--'*10)
print('CONTROLE DE TERRENOS')
print('--'*10)
l = float(input('LARGURA (m) : '))
c = float(input('COMPRIMENTO (m): '))
area(l , c)



