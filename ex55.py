#lista = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
lista = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
while True:
    n = int(input('DIGITE UM NÚMERO ENTRE 0 E 20 :'))
    if 0<= n <=20:
        break
    print('TENTE NOVAMENTE', end=' ')
print('O NÚMERO ESCOLHIDO É {} '.format(lista[n]))

