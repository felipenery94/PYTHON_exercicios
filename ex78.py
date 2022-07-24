time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('NOME DO JOGADOR :'))
    tot = int(input(f'QUANTAS PARTIDAS FEZ O JOGADOR {jogador["nome"]}'))
    partidas.clear()
    for c in range(0 , tot):
        partidas.append(int(input(f'QUANTOS GOLS O JOGADOR FEZ NA PARTIDA {c+1} ?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp= str(input('QUER CONTINUAR ? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!! DIGITE S OU N PARA RESPOSTA ')
    if resp == 'N':
        break
print('**'*30)
print('cod ', end = '')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
print('**'*30)
for k ,v in enumerate(time):
    print(f'{k:>3} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('**'*30)
while True:
    busca = int(input('DADOS DE QUAL JOGADOR VC QUER ? (999 PARA PARAR)'))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO JOGADOR NÃO ESTÁ CADASTRADO NO SISTEMA')
    else:
        print(f'***LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} ')
        for i , g in enumerate(time[busca]["gols"]):
            print(f' NO JOGO {i+1} FEZ {g} GOLS')
print('>>> VOLTE SEMPRE <<<')

