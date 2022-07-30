#include <stdio.h>
#include <math.h>

double areaCirculo(double raio) {
    const double PI = 3.14159;
    return PI*pow(raio, 2);
}

int main() {
    double raio;
    scanf("%lf", &raio);
    printf("A=%.4lf\n", areaCirculo(raio));

    return 0;
}
