print('-='*30)
print('{:*^50}'.format('LISTAGEM DE PREÇOS'))
print('-='*30)
lista = ('ARROZ', 15.99,
         'FEIJÃO',10.99,
         'ÓLEO',7.95,
         'AÇUCAR',5.25,
         'LEITE',4.99,
         'CAFÉ',11.90,
         'BOLACHA',3.25,
         'DANONE',1.99,
         'PÃO',4.50)
for pos in range(0 , len(lista)):
    if pos % 2==0:
        print(f'{lista[pos]:.<35}',end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-='*30)
