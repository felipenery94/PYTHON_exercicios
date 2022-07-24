dados = {}
pessoas = []
soma = media = 0
while True:
    dados.clear()
    dados['NOME'] = str(input('NOME : '))
    while True:
        dados['SEXO'] = str(input('SEXO [M/F]: ')).upper()[0]
        if dados['SEXO'] in 'MF':
            break
        print('ERRO VC DIGITOU ERRADO , DIGITE SEU SEXO [M/F]')
    dados['IDADE'] = int(input('IDADE : '))
    soma+= dados['IDADE']
    pessoas.append(dados.copy())
    while True:
        resp = str(input('QUER CONTINUAR S/N ?')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO ,DIGITE APENAS (S OU N')
    if resp == 'N':
        break
print('**'*30)
print(f'AO TODO TEMOS {len(pessoas)} PESSOAS CADASTRADAS')
media = soma / len(pessoas)
print(f'A MÉDIA DAS IDADES É {media:.2f} ANOS')
print(f'AS MULHERES CADASTRADAS FORAM ', end='')
for p in pessoas:
    if p['SEXO'] in 'Ff':
        print(f'{p["NOME"]}', end= ' ')
print()
print('LISTA DAS PESSOAS QUE ESTÃO ACIMA DA MÉDIA')
for p in pessoas:
    if p['IDADE'] >= media:
        print('   ')
        for k , v in p.items():
            print(f'{k} = {v}; ',end = ' ')
        print()
print('ENCERRADO')





