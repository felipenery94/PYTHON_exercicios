s = cont =0
while True:
    v = int(input('Digite um valor [ 999 PARA PARAR] :'))
    if v == 999 :
        break
    s+=v
    cont+= 1
print(f'FORAM DIGITADOS {cont} valores e a soma é {s} !')


