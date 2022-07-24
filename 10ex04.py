d = float(input('\033[4;32mqual distância de sua viajem?'))
p1= d*0.50
p2 = d*0.45
if d <200:
    print('\033[31mo valor da passagem será de r$ {:.2f} reais\n uma viajem de {}km'.format(p1,d))
else:
    print('\033[31mo valor será r$ {:.2f}\numa viajem de {:.1f}km'.format(p2,d))