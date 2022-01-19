idade = int(input())
anos = meses = dias = 0
while idade > 0:
    if idade >= 365:
        anos += 1
        idade -= 365
    elif idade >= 30:
        meses += 1
        idade -= 30
    else:
        dias += idade
        idade -= idade
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
