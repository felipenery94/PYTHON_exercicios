listanum=[]
maior = 0
menor = 0
for c in range (0,5):
    listanum.append(int(input(f'DIGITE NUMERO NA POSIÇÃO {c} : ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior :
            maior = listanum[c]
        if listanum[c] <menor :
            menor = listanum[c]
print(f'VOCE DIGITOU OS VALORES {listanum}')
print('***'*30)
print(f'O maior valor é {maior} nas posições ', end=' ')
for i, v in enumerate(listanum):
    if v == maior :
        print(f'{i}...',end= ' ')
print()
print(f'O menor valor é {menor} nas posições ',end=' ')
for i, v in enumerate(listanum):
    if v == menor :
        print(f'{i}...',end= ' ')