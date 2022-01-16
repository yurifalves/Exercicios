lista_dados1 = input().split()
total1 = int(lista_dados1[1])*float(lista_dados1[2])
lista_dados2 = input().split()
total2 = int(lista_dados2[1])*float(lista_dados2[2])

print(f'VALOR A PAGAR: R$ {(total1+total2):.2f}')
