#include <stdio.h>

int main() {
    int segundos, horas = 0, minutos = 0;
    scanf("%d", &segundos);

    while (segundos >= 3600) {
        horas += 1;
        segundos -= 3600;
    }

    while (segundos >= 60) {
        minutos += 1;
        segundos -= 60;
    }

    printf("%d:%d:%d\n", horas, minutos, segundos);

    return 0;
}
