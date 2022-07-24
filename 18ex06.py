ficha = list()
while True:
    nome = str(input('NOME : '))
    nota = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2:'))
    media = (nota + nota2) / 2
    ficha.append([nome ,[nota , nota2], media] )
    resp = str(input('QUER CONTINUAR ? [S/N]'))
    if resp in 'Nn':
        break
print('-='*20)
print('N°',     'NOME',     'MEDIA')
print('-='*30)
for i , a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True :
    print('-='*30)
    opc = int(input('MOSTRAR NOTAS DE QUAL ALUNO ? (999 para encerrar)'))
    if opc == 999:
        break
    if opc <= len(ficha)-1:
        print(f'NOTAS DE {ficha[opc][0]} SÃO {ficha[opc][1]}')
print('<<<VOLTE SEMPRE>>>')






