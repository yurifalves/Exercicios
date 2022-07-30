#include <stdio.h>

int isTriangle(double A, double B, double C);
double perimetroTriangulo(double A, double B, double C);
double areaTrapezio(double A, double B, double C);

int main() {
    double A, B, C;
    scanf("%lf", &A);
    scanf("%lf", &B);
    scanf("%lf", &C);

    if (isTriangle(A, B, C)) {
        printf("Perimetro = %.1lf\n", perimetroTriangulo(A, B, C));
    }
    else {
        printf("Area = %.1lf\n", areaTrapezio(A, B, C));
    }

    return 0;
}

int isTriangle(double A, double B, double C) {
    if (A<B+C && B<A+C && C<A+B) {
        return 1;
    }
    return 0;
}

double  perimetroTriangulo(double A, double B, double C) {
    return A+B+C;
}

double areaTrapezio(double A, double B, double C) {
    return (A+B)*C/2;
}
