aluno = dict()
aluno['nome'] = str(input('NOME: '))
aluno['media'] = float(input(f'MÉDIA DE {aluno["nome"]}:'))
if aluno['media'] >= 7 :
    aluno['situação'] = 'aprovado'
elif 5<= aluno['media'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação']= 'reporvado'
for k , v in aluno.items():
    print(f'{k} é igual a {v}')




