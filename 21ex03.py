def ficha(jog='> desconhecido<',gol=0):
    print(f'O JOGADOR {jog} FEZ {gol} GOLS NA PARTIDA')


n = str(input('NOME DO JoGADOR :'))
g = str(input('QUANTOS GOLS MARCOU ?'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip()=='':
    ficha(gol=0)
else:
    ficha(n , g)