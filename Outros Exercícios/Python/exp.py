def media(amostra):
    import statistics
    media = statistics.mean(amostra)
    return media

def desvio_padrao(amostra):
    import statistics
    desvio_padrao = statistics.pstdev(amostra)
    return desvio_padrao


def erro_aleatorio(amostra):
    import statistics, math
    desvio_padrao = statistics.pstdev(amostra)
    erro_aleatorio = desvio_padrao/math.sqrt(len(amostra))
    return erro_aleatorio
