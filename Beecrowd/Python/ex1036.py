import math
A, B, C = [float(item) for item in input().split()]
discriminante = B**2-4*A*C
if 2*A == 0 or discriminante < 0:
    print('Impossivel calcular')
else:
    R1, R2 = (-B+(math.sqrt(discriminante)))/(2*A), (-B-(math.sqrt(discriminante)))/(2*A)
    print(f'R1 = {R1:.5f}\nR2 = {R2:.5f}')
