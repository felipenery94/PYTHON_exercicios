print('OS 10 PRIMEIROS TERMOS DE UMA PA!')
print('==='*20)
primeiro= int(input('Digite o primeiro termo de um PA:'))
r = int(input('Digite razao da PA:'))
termo = primeiro
cont = 1
conte = 1
while cont <= 10:
    print('{}-'.format(termo), end = '')
    termo += r
    cont+=1
print('FIM')