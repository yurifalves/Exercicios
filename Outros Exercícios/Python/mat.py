def fib(n: int) -> int:
    """
    Retorna um número específico da Sequência de Fibonacci

    https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series/70173360#70173360
    """
    if n < 0: return int(pow(-1, (n & 1) + 1)) * fib(-n)
    if n == 0: return 0
    if n == 1 or n == 2: return 1
    if n == 3: return 2

    # n is multiple of 3
    if n % 3 == 0:
        third = n // 3
        fibthird = fib(third)
        return 5 * pow(fibthird, 3) + 3 * pow(-1, third) * fibthird

    # even n
    if n & 1 == 0:
        return pow(fib((n >> 1) + 1), 2) - pow(fib((n >> 1) - 1), 2)

    # for odd n
    return pow(fib((n >> 1) + 1), 2) + pow(fib(n >> 1), 2)


def angulo_entre_vetores(vetor_1, vetor_2):
    """
    uv = ||u|| ||v|| cos(θ)
    θ = arccos(uv/||u|| ||v||)
    
    Retorna o ângulo em graus entre dois vetores n-dimensionais.
    """
    import numpy as np

    if np.linalg.norm(vetor_1) == 0 or np.linalg.norm(vetor_2) == 0:
        return 'Vetor de magnitude zero!'

    produto_escalar = np.dot(vetor_1, vetor_2)
    norma_1 = np.linalg.norm(vetor_1)
    norma_2 = np.linalg.norm(vetor_2)

    angulo = np.degrees(np.arccos(produto_escalar/(norma_1*norma_2)))
    return angulo
