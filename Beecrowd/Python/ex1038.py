precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}
cod, quant = [int(item) for item in input().split()]
print(f'Total: R$ {precos[cod]*quant:.2f}')
