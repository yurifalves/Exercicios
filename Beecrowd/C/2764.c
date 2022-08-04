#include <stdio.h>

int main() {
    char data[8], DD[3], MM[3], AA[3];
    for (int i=0; i<8; i++) {
        scanf("%c", &data[i]);
    }

    for (int i=0; i<2; i++) {
        DD[i] = data[i];
    }
    DD[2] = '\0';

    for (int i=3; i<5; i++) {
        MM[i-3] = data[i];
    }
    MM[2] = '\0';

    for (int i=6; i<8; i++) {
        AA[i-6] = data[i];
    }
    AA[2] = '\0';

    printf("%s/%s/%s\n", MM, DD, AA);
    printf("%s/%s/%s\n", AA, MM, DD);
    printf("%s-%s-%s\n", DD, MM, AA);

    return 0;
}
