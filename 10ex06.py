v1 = int(input('\033[31mdigite um primeiro valor'))
v = int(input('\033[31mdigite um segundo valor'))
v3 = int(input('\033[31mdigite um terceiro valor'))
#verificando quem é o menor
menor = v1
if v < v1 and v < v3:
    menor = v
if v3 < v1 and v3 < v:
    menor = v3
#verificando quem é o maior
maior = v1
if v > v1 and v > v3:
    maior = v
if v3 > v1 and v3 > v:
    maior = v3
print('\033[4;32mmenor número é {}'.format(menor))
print('\033[4;32mmaior número é {}'.format(maior))
