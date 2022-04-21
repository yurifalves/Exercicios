#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    char letra;

    printf("<<< EX008 - ALFABETO >>>\n\n");
    printf("Digite uma letra: ");
    letra = getchar();
    printf("Antes da letra %c temos a letra %c e depois temos a letra %c.\n", letra, letra-1, letra+1);

    return 0;
}
