def is_triang(a, b, c):
    if a+b > c and b+c > a and a+c > b:
        return True
    return False


A, B, C = [float(num) for num in (input().split())]
if is_triang(A, B, C):
    print(f'Perimetro = {(A + B + C):.1f}')
else:
    print(f'Area = {((A*C+B*C)/2):.1f}')
