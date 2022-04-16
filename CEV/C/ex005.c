#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#include <time.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    srand(time(NULL));
    int num = rand() % 5 + 1;
    int chute;

    printf("<<< EX005 - NÚMEROS ALEATÓRIOS >>>\n\n");
    printf("Vou pensar em um número entre 1 e 5. Tente adivinhar!\n");
    printf("Qual é o seu palpite? ");
    scanf("%i", &chute);
    printf("Eu pensei no número %i e você pensou no %i.\n", num, chute);

    return 0;
}
