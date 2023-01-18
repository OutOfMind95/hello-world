#include <stdio.h>
int main(void)
{
    int num [] = {4, 5, 7, 8, 4, 3, 0};
    printf("%i\n", *num);
    printf("%i\n", *(num+1));
    printf("%i\n", *(num+2));
    printf("%i\n", *(num+3));
    printf("%i\n", *(num+4));
    printf("%i\n", *(num+5));
    printf("%i\n", *(num+6));
}