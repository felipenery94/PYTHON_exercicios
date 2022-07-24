salario = float(input('\033[33mqual salário do funcionário?r$'))
if salario <= 1250:
    novo = salario+(salario*15/100)
else:
    novo = salario+(salario*10/100)
print('\033[4;31mquem ganhava R$ {:.2f}, passa a ganhar R$ {:.2f} agora'.format(salario,novo))



