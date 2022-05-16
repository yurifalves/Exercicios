def imposto_renda(renda):
    if renda <= 2000:
        return 'Isento'
    elif renda <= 3000:
        renda -= 2000
        imposto = 0.08 * renda
        return f'R$ {imposto:.2f}'
    elif renda <= 4500:
        renda -= 2000
        imposto = 0.08*1000 + 0.18*(renda-1000)
        return f'R$ {imposto:.2f}'
    else:
        renda -= 2000
        imposto = 0.08 * 1000 + 0.18*1500 + 0.28*(renda-2500)
        return f'R$ {imposto:.2f}'


renda = float(input())
print(imposto_renda(renda))
