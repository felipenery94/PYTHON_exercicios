print('10 TERMOS DE UM PA ')
print('**'*20)
t = int(input('primeiro termo'))
r = int(input('razão'))
decimo = t + (10 - 1 ) * r
for c in range(t ,decimo + r , r):
    print('{}'.format(c), end= ' ')