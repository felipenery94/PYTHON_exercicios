from datetime import date
id = int(input('digite seu ano de nascimento '))
ano = date.today().year - id
if ano <= 9:
    print('''Atleta tem {} anos,'
'Classificação:  mirim.'''.format (ano))
elif ano > 9 and ano < 14 or ano == 14:
    print('''Atleta tem {} anos ,
Classsificação infantil'''.format(ano))
elif ano > 15 and ano < 19 or ano == 19:
    print('''Atleta tem {} anos 
Classificação : junior'''.format (ano))
elif ano > 19 and ano < 25 or ano ==25:
    print('''Atleta tem {} anos
Classificação : sênior'''.format (ano))
else:
    print('''Atleta tem {} anos 
Classificação : master'''.format (ano))

