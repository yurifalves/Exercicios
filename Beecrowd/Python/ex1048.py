class Funcionario:

    def __init__(self, salario: float):
        if salario <= 400:
            self.reajuste = 0.15
        elif salario <= 800:
            self.reajuste = 0.12
        elif salario <= 1200:
            self.reajuste = 0.1
        elif salario <= 2000:
            self.reajuste = 0.07
        else:
            self.reajuste = 0.04
        self.novo_salario = salario + self.reajuste*salario
        self.reajuste_percentual = int(100*self.reajuste)
        self.reajuste_ganho = self.novo_salario - salario


salario = float(input())
pessoa = Funcionario(salario)
print(f'Novo salario: {pessoa.novo_salario:.2f}')
print(f'Reajuste ganho: {pessoa.reajuste_ganho:.2f}')
print(f'Em percentual: {pessoa.reajuste_percentual} %')
