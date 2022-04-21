def analisar_horas(a, b):
    duracao = (24-a) + b
    while duracao > 24:
        duracao -= 24
    print(f'O JOGO DUROU {duracao} HORA(S)')


hora_inicial, hora_final = [int(hora) for hora in input().split()]
analisar_horas(hora_inicial, hora_final)
