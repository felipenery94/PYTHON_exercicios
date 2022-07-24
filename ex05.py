p = float(input('\033[31mproduto R$'))
va = p-(p*10/100)
vp = p+(p*15/100)
print('\033[4;36mo produto custa r$ {:.2f}, à vista terá 10% de desconto R$ {:.2f},\n '
      '\033[4;35ma prazo será 15% mais caro R${:.2f}.'.format(p,va,vp))


