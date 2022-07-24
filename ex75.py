from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input(' NOME :'))
nasc= int(input('ANO DE NASCIMENTO :'))
cadastro['idade'] = datetime.now().year - nasc
cadastro['cpts'] = int(input(' N° CARTEIRA DE TRABALHO (0 NÃO TEM):'))
if cadastro['cpts'] != 0:
    cadastro['contratação'] = int(input('ANO DE CONTRATAÇÃO :'))
    cadastro['salário'] = float(input('SALÁRIO :'))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratação'] + 35) - datetime.now().year)
print('**'*30)
for k , v in cadastro.items():
    print(f'-{k} = {v}')
