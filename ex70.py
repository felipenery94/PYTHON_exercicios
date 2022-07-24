matrix = [[0,0,0], [0,0,0], [0,0,0]]
somap = somac = mai = 0
for l in range(0,3):
    for c in range(0,3):
        matrix[l][c] = int(input(f'DIGITE UM VALOR [{l}, {c}]'))
print('-='*30)
for l in range(0,3):
    for c in range (0,3):
        print(f'[{matrix[l][c]:^5}]',end='')
        if matrix[l][c] % 2 == 0:
            somap += matrix [l][c]
    print()
print(f'A SOMA DOS VALORES PARES É {somap}')
for l in range(0,3):
    somac+= matrix[l][2]
print(f'A SOMA DOS VALORES DA TERCEIRA COLUNA É {somac}')
for c in range(0,3):
    if c ==0:
        mai =matrix [1][c]
    elif matrix[1][c]> mai :
        mai = matrix[1][c]
print(f'O MAIOR VALOR DA SEGUNDA LINHA É {mai}')

