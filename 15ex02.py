cont = 0
mult = 0
t = 1
while True:
    t = int(input('QUAL TABUADA QUER VER O VALOR ?'))
    print('----' * 20)
    if t < 0:
        break
    for cont in range(1,11):
        mult = t*cont
        print(f'{t} x {cont} = {mult}')
    print('----'*20)
print('PROGRAMA ENCERRADO')