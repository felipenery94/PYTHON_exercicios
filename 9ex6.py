n = str(input('\033[31mdigite seu nome completo ')).upper().strip()
nome = n.split()
print('\033[33mmuito prazer em te conhecer')
print('Seu primeiro nome é {}'.format(nome[0]))
print('seu ultimno nome é {}'.format(nome[len(nome)-1]))

