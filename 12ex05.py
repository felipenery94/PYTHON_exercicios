n1 = float(input('primeira nota'))
n2 = float(input('segunda nota'))
m = (n1 + n2 ) / 2
if m < 5.0:
    print('nota {:.1f} , você está REPROVADO!!!'.format(m))
elif m >=7.0:
    print('nota {:.1f}, parabéns você está APROVADO'.format(m))
else:
    print('nota {:.1f} , você está de RECUPERAÇÃO!!'.format(m))
