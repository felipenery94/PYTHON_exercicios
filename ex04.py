p = float(input('\033[34mvalor produto'))
vd = p-(p*5/100)
print('\033[4;31mo produto custa R$ {:.2f}, e com desconto de 15% , ficará R$ {:.2f}'.format(p,vd))
