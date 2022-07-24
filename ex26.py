p = float(input('Qual seu peso (kg) ?'))
a = float(input('Qual sua altura ?'))
imc = p / (a**2)
if imc < 18.5 :
    print('o seu imc é {:.1f} voçê está abaixo de peso'.format(imc))
elif imc <= 25.0 :
    print('o seu imc é {:.1f} ,Você está no peso ideal'.format(imc))
elif imc <= 30.0 :
    print('o seu imc é {:.1f}, você está com sobrepeso'.format(imc))
elif imc <= 40.0 :
    print('o seu imc é {:.1f}, você esta com obesidade'.format(imc))
elif imc >= 40.0 :
    print('o seu imc é {:.1f}, você está com obesidade morbida'.format(imc))
