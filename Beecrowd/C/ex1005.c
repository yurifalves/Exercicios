#include <stdio.h>
#define media(nota1, nota2) (3.5*nota1+7.5*nota2)/11.0

int main() {
    double nota1, nota2;
    scanf("%f", &nota1);
    scanf("%f", &nota2);
    printf("MEDIA = %.5lf\n", media(nota1, nota2));

    return 0;
}
