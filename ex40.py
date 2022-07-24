s = str(input('Qual seu sexo ? [M/F]')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Sexo incorreto , digite novamente :')).strip().upper()[0]
print('sexo {} , correto'.format(s))