def is_par(num: int) -> bool:
    if num%2 == 0: return True
    else: return False



def tirar_simb(texto: str) -> str:
    simbolos_totais = texto.count('$')
    cont = 0
    while True:
        if texto.count('$') == 0: break
        else:
            indice_simbolo = texto.index('$')
            if is_par(cont):
                texto = texto[:indice_simbolo+1].replace('$', '\(') + texto[indice_simbolo+1:]
            else:
                texto = texto[:indice_simbolo+1].replace('$', '\)') + texto[indice_simbolo+1:]
        cont += 1
    return texto
