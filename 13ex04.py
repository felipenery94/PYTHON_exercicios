#cont = 0
#soma = 0
#for c in range(1 , 501, 2):
 #if c % 3 ==0:
       # cont = cont + 1
        #soma = soma + c
#print('A soma de todos os {}  valores é {}'.format(cont , soma))
cont = 0
soma = 0
for c in range(1 , 1001 , 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores é {}'.format(cont , soma))

