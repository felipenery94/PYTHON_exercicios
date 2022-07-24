print('Analisador de triângulos')
a = float(input('digite o primeiro segmento'))
b = float(input('digite o segundo segmento'))
c = float(input('digite o terceiro segmento'))
if a < b + c and b < a + c and c < a + c :
    print(' segmentos podem formar um triângulo')
    if a == b == c :
        print('triangulo equilatero')
    elif a != b != c != a :
        print(' triangulo escaleno')
    else:
        print('triangulo isósceles')
else :
        print('segmentos não podem formar um triângulo')

