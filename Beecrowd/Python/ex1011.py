def area_esf(r):
    pi = 3.14159
    return (4/3)*pi*r**3


raio = int(input())
print(f'VOLUME = {area_esf(raio):.3f}')
