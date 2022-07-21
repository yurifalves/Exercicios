#include <stdio.h>
#include <math.h>

float distanciaPontos(float P1[], float P2[]);

int main() {
    float P1[2], P2[2];
    scanf("%f", &P1[0]);
    scanf("%f", &P1[1]);
    scanf("%f", &P2[0]);
    scanf("%f", &P2[1]);

    printf("%.4f", distanciaPontos(P1, P2));

    return 0;
}

float distanciaPontos(float P1[], float P2[]) {
    float x1 = P1[0];
    float y1 = P1[1];
    float x2 = P2[0];
    float y2 = P2[1];
    float distancia = sqrtf(powf(x2-x1, 2)+powf(y2-y1, 2));

    return distancia;
}
