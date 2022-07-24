jogador = {}
partidas = []
jogador['nome'] = str(input('NOME DO JOGADOR :'))
tot = int(input(f'QUANTAS PARTIDAS FEZ O JOGADOR {jogador["nome"]}'))
for c in range(0 , tot):
    partidas.append(int(input(f'QUANTOS GOLS O JOGADOR FEZ NA PARTIDA {c+1} ?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('**'*30)
for k , v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('**'*30)
print(f'O JOGADOR {jogador["nome"]} JOGOU {len(jogador["gols"])} PARTIDAS')
for i , v in enumerate(jogador['gols']):
    print(f'====> NA PARTIDA {i+1} FEZ {v} GOLS ')
print(f'FOI UM TOTAL DE {jogador["total"]} GOLS')
