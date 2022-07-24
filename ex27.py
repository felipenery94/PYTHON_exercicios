p = float(input('valor do produto'))
a = p - (p*10/100)
ac = p - (p*5/100)
pc = p + (p*20/100)
print('''qual forma de pagamento'
[1] à vista :'
[2] à vista no cartão:'
[3] parcelado duas vezes:'
[4] parcelado em 3 vezes ou mais' :
''')
f = int(input('qual opção de pagamento?'))

if f == 1:
    print('produto R${:.2f}, à vista/cheque terá 10% de desconto e saíra por R${:.2f}'.format(p, a ))
elif f == 2:
    print('produto R${:.2f}, à vista no cartão de crédito terá 5% de desconto e saíra por R$ {:.2f}'.format(p, ac))
elif f== 3 :
    p2 = p/2
    print('produto R$ {:.2f}, parcelado duas vezes será R${} x 2 e custará no total de  R$ {:.2f}.'.format(p,p2 ,p ))
elif f == 4 :
    cred = int(input('quantas vezes no cartão?'))
    parc = pc / cred
    print('produto R$ {:.2f}, parcelado saíra por R$ {:.2f} x {} , total de R${:.2f} no final'.format(p,parc,cred ,pc))
else:
    print('\033[32m OPÇÃO ERRADA!!')

