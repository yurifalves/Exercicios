#include <stdio.h>
#include <locale.h>
int main() {
    setlocale(LC_ALL, "Portuguese");
    printf("<<< EX002 - Especiais >>>\n\n");
    printf("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
    printf("\\a\t= \tBeep\n");
    printf("\\n\t= \tNova linha\n");
    printf("\\t\t= \tTabulação\n");
    printf("\\\\\t= \tContrabarra\n");
    printf("%%%%\t= \tPorcentagem\n");
    printf("\\\?\t= \tInterrogação\n");
    printf("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
    return 0;
}
