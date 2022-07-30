#include <stdio.h>

int main() {
    int numero, horasTrabalhadas;
    double valorHora;
    scanf("%d%d%lf", &numero, &horasTrabalhadas, &valorHora);
    printf("NUMBER = %d\n", numero);
    printf("SALARY = U$ %.2lf\n", horasTrabalhadas*valorHora);

    return 0;
}
