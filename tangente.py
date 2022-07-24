import math
a = float(input('digite o angulo que deseja'))
s = math.sin(math.radians(a))
print('o seno é {:.2f}'.format(s))
co = math.cos(math.radians(a))
print('cosseno é {:.2f}'.format(co))
t = math.tan(math.radians(a))
print('tangente é {:.2f}'.format(t))