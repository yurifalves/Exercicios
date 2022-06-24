import numpy as np


def texto_para_matriz(texto):
    """

    Converte um texto para uma matriz, eliminando espaços e quebras de linha em excesso.

    Ex:

    '''
    1 2    3 7        np.array([[1, 2, 3, 7],
    4  5 6  20   --->           [4, 5, 6, 20],
    7 8 9   1                   [7, 8, 9, 1]])
    '''

    :param texto: string no formato

    a11 a12 ... a1n
    a21 a22 ... a2n
    am1 am2 ... amn

    :return: matriz no formato

    np.array([[a11, a12, ... a1n],
              [a21, a22, ... a2n],
              [a31, a32, ... amn]])

    """
    
    def remove_element(element, the_list):
        while element in the_list: the_list.remove(element)
        return the_list

    vetores_linha_str = remove_element('', texto.splitlines())  # ['4 11 62', '-8 0 1', '3 3 0']
    vetores_linha = [np.fromstring(linha, sep=' ') for linha in vetores_linha_str]  # [array([ 4., 11., 62.]), array([-8.,  0.,  1.]), array([3., 3., 0.])]
    matriz = np.array(vetores_linha)
    return matriz
