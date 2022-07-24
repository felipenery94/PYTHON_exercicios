lista = ('CORINTHIANS','SÃO PAULO','SANTOS','PALMEIRAS','BRAGANTINO',
         'FLAMENGO','FLUMINENSE','BOTAFOGO','ATLÉTICO MINEIRO',
         'CORITIBA','ATLÉTICO PARANAENSE','FORTALEZA','CEÁRA',
         'AMÉRICA MINEIRO','AVAÍ','GOÍAS','ATL GOIANIENSE',
         'CUÍABA','INTERNACIONAL','JUVENTUDE')
print(f'LISTA DE TIMES {lista}')
print('**'*40)
print('OS CINCO PRIMEIROS TIMES SÃO: {}'.format(lista[0:5]))
print('**'*40)
print('OS QUATRO ULTIMOS COLOCADOS SÃO: {}'.format(lista[16:]))
print('**'*40)
print('AVAÍ ESTÁ NA {}° POSIÇÃO'.format(lista.index('AVAÍ')+1))
print('**'*40)
print('TIME EM ORDEM ALFABÉTICA {}'.format(sorted(lista)))
print('**'*60)
