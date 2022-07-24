lista = [[], []]
valor = 0
for c in range(0,7):
    valor = int(input(f'DIGITE {c}° VALOR : '))
    if valor %2 ==0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('-='*30)
lista[0].sort()
lista[1].sort()
print(f'OS VALORES PARES SÃO {lista[0]}')
print(f'OS VALORES ÍMPARES SÃO {lista[1]}')




