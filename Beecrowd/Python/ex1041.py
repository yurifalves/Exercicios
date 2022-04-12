def quadrante(x, y):
    if x == y == 0:
        return 'Origem'
    if x == 0:
        return 'Eixo Y'
    if y == 0:
        return 'Eixo X'

    if x > 0:
        if y > 0:
            return 'Q1'
        if y < 0:
            return 'Q4'
    else:
        if y > 0:
            return 'Q2'
        if y < 0:
            return 'Q3'


x, y = [float(num) for num in input().split()]
print(quadrante(x, y))
