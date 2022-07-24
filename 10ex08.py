print('\033[31mAnalisador de triângulos')
print('==x=='*20)
ps = float(input('Diga o primeiro segmento.'))
ss = float(input('diga o segundo segmento.'))
ts = float(input('diga o terceiro segmento.'))
if (ps + ss > ts):
    print('\033[4;34mos segmentos podem formar um trinângulo')
else:
    print('não podem formar um triângulo')
#if s > ts :
    #print('os segmentos acima podem formar um triângulo')
#else:
   # print('segmentos acima não podem formar um triângulo')
