#include <stdio.h>

int main() {
    char nomeVendedor[50];
    double salarioFixo, vendasEfetuadas;
    fgets(nomeVendedor, sizeof(nomeVendedor), stdin);
    scanf("%lf%lf", &salarioFixo, &vendasEfetuadas);

    double salarioTotal = salarioFixo + 0.15*vendasEfetuadas;
    printf("TOTAL = R$ %.2lf\n", salarioTotal);

    return 0;
}
