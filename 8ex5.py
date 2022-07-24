from random import shuffle
p1 = (input('primeiro nome'))
p2 = (input('segundo nome'))
p3 = (input('terceiro nome'))
p4 = (input('quarto nome'))
ordem = [p1,p2,p3,p4]
shuffle(ordem)
print('a ordem será{}'.format(ordem))

