#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(0, "Portuguese");
    int a, b;

    printf("<<< EX013 - OPERADORES BITWISE >>>\n\n");
    printf("Digite o primeiro valor: ");
    scanf("%d", &a);
    printf("Digite o segundo valor: ");
    scanf("%d", &b);
    printf("------ OPERAÇÕES BITWISE ------\n");
    printf("%d & %d é igual a %d\n", a, b, a&b);
    printf("%d | %d é igual a %d\n", a, b, a|b);
    printf("%d ^ %d é igual a %d\n", a, b, a^b);

    return 0;
}
