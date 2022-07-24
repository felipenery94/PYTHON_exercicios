print('-='*30)
palavras = ('mercado','laranja','hospital',
            'academia','celular','praia',
            'bicicleta','abacaxi','computador')
for p in palavras:
    print(f'\nNA PALAVRA {p.upper()} TEMOS ', end = ' ')
    for letra in p:
        if letra in 'aeiou' :
            print(letra , end = ' ')