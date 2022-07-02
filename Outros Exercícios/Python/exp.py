def media(amostra):
    import statistics
    media = statistics.mean(amostra)
    return media


def desvio_padrao(amostra):
    import numpy as np
    array = np.array(amostra)
    desvio_padrao = np.std(array, ddof=1)  # Desvio padrão com N-1 ao invés de N
    return desvio_padrao


def erro_aleatorio(amostra):
    import statistics, math
    desvio_padrao = statistics.pstdev(amostra)
    erro_aleatorio = desvio_padrao/math.sqrt(len(amostra))
    return erro_aleatorio
