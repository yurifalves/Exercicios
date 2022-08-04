lista_original = [int(num) for num in input().split()]
lista_crescente = lista_original.copy()
lista_crescente.sort()

for num in lista_crescente:
    print(num)
print()
for num in lista_original:
    print(num)
