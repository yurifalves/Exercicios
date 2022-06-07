#include <stdio.h>

int main() {
    double nota1, nota2, nota3;
    scanf("%lf%lf%lf", &nota1, &nota2, &nota3);
    double media = (double)(2*nota1+3*nota2+5*nota3)/10;
    printf("MEDIA = %.1lf\n", media);

    return 0;
}
