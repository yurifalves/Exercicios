tempo_horas = int(input())
vel_kmh = int(input())
distancia_km = tempo_horas*vel_kmh
quantidade_litros = distancia_km/12
print(f'{quantidade_litros:.3f}')
