from datetime import date
i = int(input('ano de nascimento?'))
a = date.today().year
b = a - i
c = 18 - b
d = b - 18
e = a + c
f = a - d
if b < 18:
  print('{} anos de idade nao necessita se alistar ,faltam {} anos para o alistamento, volte em {} ao exercito'.format(b,c,e))
elif b ==18:
    print('{} anos , terá que se alistar IMEDIATAMENTE!!'.format(b))
else:
    print('{} anos de idade, passou da hora , seu alistamento foi em {}, está {} anos atrasado!!'.format(b,f,d))



