#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long n = get_long ("n: ");

    //If n is even
    if (n % 2 == 0)
    {
        printf("even\n");
    }
    else
    {
        printf("odd\n");
    }
}