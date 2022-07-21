#include <stdio.h>

double impostoDeRenda(double salario) {
    if (salario <= 3000) {
        salario -= 2000;
        double imposto = 0.08*salario;
        return imposto;
    }
    else if (salario <=4500) {
        salario -= 2000;
        double imposto = 0.08*1000 + 0.18*(salario-1000);
        return imposto;
    }
    else {
        salario -= 2000;
        double imposto = 0.08*1000 + 0.18*1500 + 0.28*(salario-2500);
        return imposto;
    }
}

int main() {
    double salario;
    scanf("%lf", &salario);

    if (salario <= 2000) {
        printf("Isento\n");
    }
    else {
        printf("R$ %.2lf\n", impostoDeRenda(salario));
    }

    return 0;
}
