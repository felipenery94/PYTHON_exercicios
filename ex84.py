def voto(ano):
    from _datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'COM {idade} ANOS : NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'COM {idade} ANOS : VOTO OPCIONAL'
    else:
        return f'COM {idade} ANOS : VOTO OBRIGATÓRIO'

nas = int( input('EM QUAL ANO VOÇÊ NASCEU ? '))
print(voto(nas))

