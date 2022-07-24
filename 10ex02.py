v = float(input('qual a velocidade atual do veículo?'))
m = (v-80)*7
if v >80:
    print('\033[31mATENÇÃO!!!!')
    print('\033[4;33mvocê será multado em {} \n ultrapassou o limite de velocidade de 80km/h!'.format(m))
    print('Tenha mais cuidado da próxima vez.')
else:
    print('ok, dirija com cuidado!!!')
