somaidade=0
mediaidade=0
maioridadehomem=0
nomevelho =0
totmulher20=0
for p in range(1,5):
    print('{}° PESSOA'.format(p))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade :'))
    sexo = str(input('sexo [M/F]:')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm'and idade > maioridadehomem:
        maioridadehomem =  idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20 :
        totmulher20 += 1
mediaidade = somaidade/4
print('media de idade é {} anos'.format(mediaidade))
print('o homem mais velho é {} e tem {} anos '.format(nomevelho , maioridadehomem))
print('O total de mulheres com menos de 20 anos é {}'.format(totmulher20))