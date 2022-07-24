al = int (input('\033[31mquantiidade de dias alugados'))
kmp = float(input('\033[31mquantidade de km rodado'))
vt = (al * 60) + (kmp * 0.15)
print('\033[4;32m valor total a ser pago pelo aluguel é de {:.2f} r$'.format(vt))


