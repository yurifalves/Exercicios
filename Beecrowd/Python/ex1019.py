import time
a = time.gmtime(int(input()))
if a[2] > 1:
    hora = minuto = segundo = 0
    for i in range(a[2]-1):
        hora += 24
    hora += a[3]
    minuto = a[4]
    segundo = a[5]
    print(f'{hora}:{minuto}:{segundo}')
else:
    print(f'{a[3]}:{a[4]}:{a[5]}')
