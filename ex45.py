print('GERADOR DE PA')
print('***'*20)
primeiro = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Qual a razão :'))
termo  = primeiro
c = 1
total = 0
mais  = 10
while mais !=0:
    total += mais
    while c <= total :
        print('{}'.format(termo), end = '-')
        termo += razao
        c+=1
    print('pausa')
    mais  =  int(input('mais termos'))
print('PROGRESSAO FINALIZADA COM {} , TERMOS .'.format(total))




