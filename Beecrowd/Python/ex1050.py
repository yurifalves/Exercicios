def classificar_ddd(ddd):
    if ddd == '61': return 'Brasilia'
    elif ddd == '71': return 'Salvador'
    elif ddd == '11': return 'Sao Paulo'
    elif ddd == '21': return 'Rio de Janeiro'
    elif ddd == '32': return 'Juiz de Fora'
    elif ddd == '19': return 'Campinas'
    elif ddd == '27': return 'Vitoria'
    elif ddd == '31': return 'Belo Horizonte'
    else: return 'DDD nao cadastrado'


ddd = input()
print(classificar_ddd(ddd))
