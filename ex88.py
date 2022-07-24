def notas(*n , sit=False):
    """
    FUNÇÃO PARA CALCULAR NOTAS DOS ALUNOS DA ESCOLA
    :param n: QUANTIDADE DE NOTAS POR ALUNO
    :param sit: SITUAÇÃO OPCIONAL , QUE MOSTRA QUAL SITUAÇÃO DAS NOTAS DO ALUNO NA ESCOLA
    :return: DICIONÁRIO COM VARIAS SITUAÇÕES DA TURMA
    """
    r = dict()
    r ['total'] = len(n)
    r ['maior'] = max(n)
    r ['menor'] = min(n)
    r  ['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r

resp = notas(9, 2 , 5 , 4 , sit=True)
print(resp)
help(notas)
