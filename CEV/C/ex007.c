#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    int num;

    printf("<<< EX007 - DOBRO E TERÇA PARTE >>>\n\n");
    printf("Digite um número: ");
    scanf("%i", &num);
    int dobro = 2*num;
    float terco = num/3.0;
    printf("Analisando o número %i, seu dobro é %i e sua terça parte é %.2f.\n", num, dobro, terco);

    return 0;
}
