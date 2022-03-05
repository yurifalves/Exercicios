def checkinterval(a, b):
    """
    Esta função checa dentro de um intervalo fechado [a, b] sendo a e b números naturais,
    quais números são primos e quais são compostos.
    :param a: Início do intervalo a ser analisado.
    :param b: Fim do Intervalo a ser analisado.
    :return: 2 listas, uma com os números primos e outra com os números compostos. Abaixo aparecerá o tempo de execução.
    """
    from tqdm import tqdm
    import time
    start_time = time.time()
    if a < 0 or a > b:
        return f'alguma condição está sendo violada: a < 0 ou a < b'
    else:
        listaprimos = []
        listacompostos = []
        for n in tqdm(range(a, b+1)):
            cont = 0
            for t in range(1, n+1):
                if n % t == 0:
                    cont += 1
            if cont == 2:
                listaprimos.append(n)
            else:
                listacompostos.append(n)
        return f'CONSIDERANDO O INTERVALO [{a}, {b}]\nNÚMEROS PRIMOS: {listaprimos}' \
               f'\nNÚMEROS COMPOSTOS: {listacompostos}\nTEMPO DE EXECUÇÃO: {time.time() - start_time} s'
