#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    int num;

    printf("<<< EX006 - ANTECESSOR e SUCESSOR >>>\n\n");
    printf("Digite um número: ");
    fflush(stdin);
    scanf("%i", &num);
    printf("Analisando o número %i, seu antecessor é %i e o sucessor é %i.\n", num, num-1, num+1);

    return 0;
}
