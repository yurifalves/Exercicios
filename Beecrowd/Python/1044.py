def is_multp(a, b):
    if a % b == 0 or b % a == 0:
        return 'Sao Multiplos'
    return 'Nao sao Multiplos'


A, B = [int(num) for num in input().split()]
print(is_multp(A, B))
