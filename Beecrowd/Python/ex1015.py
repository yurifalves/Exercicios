def distancia_pontos(ab1, od1, ab2, od2):
    """
    :param ab1: abcissa1 (x1)
    :param od1: ordenada1 (y2)
    :param ab2: abcissa2 (x2)
    :param od2: ordenada2 (y2)
    :return: Distãncia entre dois pontos no plano.
    """
    import math
    distancia = math.sqrt((ab2-ab1)**2+(od2-od1)**2)
    return distancia


entrada_1 = input()
x1, y1 = [float(z) for z in entrada_1.split()]
entrada_2 = input()
x2, y2 = [float(z) for z in entrada_2.split()]

print(f'{distancia_pontos(x1, y1, x2, y2):.4f}')
