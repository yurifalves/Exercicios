#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    printf("<<< EX028 - SUPER CALCULADORA v1.0 >>>\n");
    int valor1, valor2;
    printf("Valor 1 = ");
    fflush(stdin);
    scanf("%d", &valor1);

    printf("Valor 2 = ");
    fflush(stdin);
    scanf("%d", &valor2);
    for (int i = 1; i<=22; i++) {
        printf("=");
    }
    printf("\n+        Adição\n");
    printf("-        Subtração\n");
    printf("*        Multiplicação\n");
    printf("/        Divisão\n");
    for (int i = 1; i<=22; i++) {
        printf("=");
    }
    printf("\nDigite sua opção => ");

    char opcao;
    fflush(stdin);
    scanf("%c", &opcao);

    switch (opcao) {
        case '+':
            for (int i = 1; i<=40; i++) {
                printf("-");
            }
            printf("\nO resultado de %d + %d é igual a %d\n", valor1, valor2, valor1+valor2);
            for (int i = 1; i<=40; i++) {
                printf("-");
            }
            printf("\n");
            break;
        case '-':
            for (int i = 1; i<=40; i++) {
                printf("-");
            }
            printf("\nO resultado de %d - %d é igual a %d\n", valor1, valor2, valor1-valor2);
            for (int i = 1; i<=40; i++) {
                printf("-");
            }
            printf("\n");
            break;
        case '*':
            for (int i = 1; i<=40; i++) {
                printf("-");
            }
            printf("\nO resultado de %d * %d é igual a %d\n", valor1, valor2, valor1*valor2);
            for (int i = 1; i<=40; i++) {
                printf("-");
            }
            printf("\n");
            break;
        case '/':
            for (int i = 1; i<=40; i++) {
                printf("-");
            }
            printf("\nO resultado de %d / %d é igual a %.2f\n", valor1, valor2, (float)valor1/valor2);
            for (int i = 1; i<=40; i++) {
                printf("-");
            }
            printf("\n");
            break;
        default:
            for (int i = 1; i<=40; i++) {
                printf("-");
            }
            printf("\nNão foi possível fazer a operação. Tente novamente\n");
            for (int i = 1; i<=40; i++) {
                printf("-");
            }
            printf("\n");
    }

    return 0;
}
