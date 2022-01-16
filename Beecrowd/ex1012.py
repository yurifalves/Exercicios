entrada = input()
A, B, C = entrada.split()  # Unpacking de lista
A, B, C = float(A), float(B), float(C)

pi = 3.14159
triang_retang = (A * C)/2
circ = pi * C**2
trap = ((A+B)*C)/2
quad = B**2
ret = A * B

print(f'TRIANGULO: {triang_retang:.3f}')
print(f'CIRCULO: {circ:.3f}')
print(f'TRAPEZIO: {trap:.3f}')
print(f'QUADRADO: {quad:.3f}')
print(f'RETANGULO: {ret:.3f}')
