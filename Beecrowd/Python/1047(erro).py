def calcular_tempo(h_inicial: int, m_inicial: int, h_final: int, m_final: int) -> tuple:
    variacao_horas, variacao_minutos = (h_final-h_inicial, m_final-m_inicial)

    if variacao_horas == 0:
        if variacao_minutos == 0:
            variacao_horas, variacao_minutos = (24, 0)
        elif variacao_minutos < 0:
            variacao_horas = 23
            variacao_minutos *= -1
        else:
            pass
    elif variacao_horas < 0:
        variacao_horas += 24
        if m_final < m_inicial:
            variacao_horas -= 1
            variacao_minutos += 60
        else:
            pass
    else:
        if m_final < m_inicial:
            variacao_horas -= 1
            variacao_minutos += 60
        else:
            pass

    return variacao_horas, variacao_minutos


h_inicial, m_inicial, h_final, m_final = [int(num) for num in input().split()]
variacao_horas, variacao_minutos = calcular_tempo(h_inicial, m_inicial, h_final, m_final)
print(f'O JOGO DUROU {variacao_horas} HORA(S) E {variacao_minutos} MINUTO(S)')
