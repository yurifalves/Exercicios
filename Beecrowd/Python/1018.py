valor = valor_total = int(input())
nota_100 = nota_50 = nota_20 = nota_10 = nota_5 = nota_2 = nota_1 = 0
while valor >= 100:
    nota_100 += 1
    valor -= 100
while valor >= 50:
    nota_50 += 1
    valor -= 50
while valor >= 20:
    nota_20 += 1
    valor -= 20
while valor >= 10:
    nota_10 += 1
    valor -= 10
while valor >= 5:
    nota_5 += 1
    valor -= 5
while valor >= 2:
    nota_2 += 1
    valor -= 2
while valor >= 1:
    nota_1 += 1
    valor -= 1
print(f'''{valor_total}
{nota_100} nota(s) de R$ 100,00
{nota_50} nota(s) de R$ 50,00
{nota_20} nota(s) de R$ 20,00
{nota_10} nota(s) de R$ 10,00
{nota_5} nota(s) de R$ 5,00
{nota_2} nota(s) de R$ 2,00
{nota_1} nota(s) de R$ 1,00''')
