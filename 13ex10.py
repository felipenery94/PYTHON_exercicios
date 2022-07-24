from datetime import date
contmaior = 0
contmenor= 0
ano = date.today().year
for c in range(1 , 8 ):
    a = int(input('Em que ano a {}° pessoa nasceu?'.format(c)))
    idade = ano - a
    if idade >= 18:
        contmaior +=1
    else:
        contmenor +=1
print('{} maior de idade'.format(contmaior))
print('{} menor de idade'.format(contmenor))

