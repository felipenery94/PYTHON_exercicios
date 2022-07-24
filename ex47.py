n = 0
cont = 0
somar = 0
while n != 999 :
    n = int(input('DIGITE UM NÚMERO [999] PARA PARAR :'))
    if n != 999:
        cont+=1
        somar += n
print('A SOMA DOS {} TERMOS É {} '.format(cont, somar))
print('FIM')