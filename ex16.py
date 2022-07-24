from datetime import date
a = int(input('\033[4;031mdiga um ano?''coloque 0 para analisar ano atual'))
if a == 0:
    a = date.today().year
if a % 4 ==0 and a % 100 !=0 or a % 400==0:
    print('\033[33mano {} é bissexto'.format(a))
else:
    print('\033[33m{} não é bissexto'.format(a))