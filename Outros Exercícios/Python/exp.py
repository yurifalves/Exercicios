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
    import math
    erro_aleatorio = desvio_padrao(amostra)/math.sqrt(len(amostra))
    return erro_aleatorio


amostra = [x1, x2, x3, ...]
print(media(amostra))
print(desvio_padrao(amostra))
print(erro_aleatorio(amostra))
