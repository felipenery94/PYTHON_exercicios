m = [[0,0,0], [0,0,0],[0,0,0]]
for l in range (0 , 3):
    for c in range(0, 3 ):
        m[l][c] = int(input(f'DIGITE UM VALOR PARA [{l} , {c}]'))
print('-='*30)
for l in range(0 , 3):
    for c in range (0 , 3):
        print(f'[{m[l][c]:^5}]', end=' ')
    print()



