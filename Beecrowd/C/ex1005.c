#include <stdio.h>

double media(double nota1, double nota2) {
    return (3.5*nota1+7.5*nota2)/11.0;
}

int main() {
    double nota1, nota2;
    scanf("%lf", &nota1);
    scanf("%lf", &nota2);
    printf("MEDIA = %.5lf\n", media(nota1, nota2));

    return 0;
}
