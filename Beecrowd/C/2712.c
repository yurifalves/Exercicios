#include <stdio.h>
#include <string.h>
#include <ctype.h>

int verificarPlaca(char placa[]);

int main() {
    int N;
    scanf("%d", &N);

    for (int i=0; i<N; i++) {
        char placa[101];
        scanf(" %[^\n]", placa);
        switch (verificarPlaca(placa)) {
            case 0:
                printf("FAILURE\n");
                break;
            case 1:
                printf("MONDAY\n");
                break;
            case 2:
                printf("TUESDAY\n");
                break;
            case 3:
                printf("WEDNESDAY\n");
                break;
            case 4:
                printf("THURSDAY\n");
                break;
            case 5:
                printf("FRIDAY\n");
                break;
        }
    }
    return 0;
}

int verificarPlaca(char placa[]) {
    int tamString = strlen(placa);

    if (tamString == 8 && isupper(placa[0]) && isupper(placa[1])
        && isupper(placa[2]) && placa[3] == '-' && isdigit(placa[4])
        && isdigit(placa[5]) && isdigit(placa[6]) && isdigit(placa[7])) {
        if (placa[tamString-1]=='1' || placa[tamString-1]=='2') return 1;
        if (placa[tamString-1]=='3' || placa[tamString-1]=='4') return 2;
        if (placa[tamString-1]=='5' || placa[tamString-1]=='6') return 3;
        if (placa[tamString-1]=='7' || placa[tamString-1]=='8') return 4;
        if (placa[tamString-1]=='9' || placa[tamString-1]=='0') return 5;
    }
    else {
        return 0;
    }
}
