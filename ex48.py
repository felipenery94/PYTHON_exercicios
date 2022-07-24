resp = 'Ss'
soma = quant = media = maior = menor =0
while resp in 'Ss':
    num = int(input('DIGITE UM NÚMERO :'))
    soma += num
    quant +=1
    if quant == 1 :
        maior = menor = num
    else:
        if num > maior :
            maior = num
        if num < menor:
            menor = num


    resp = str(input('QUER CONTINUAR ? [S/N]')).upper()
media = soma /quant
print('VOCE DIGITOU {} números , E A MÉDIA É {}'.format(quant, media))
print('MAIOR NÚMERO É {} E MENOR {}'.format(maior, menor))

