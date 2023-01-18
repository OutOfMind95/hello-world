#include <cs50.h>
#include <stdio.h>

int increment(int x);

int main(void)
{
    int x = 1; // x è locale per main
    int y;
    y = increment(x); // call the function
    printf("x is %i, y is %i\n", x, y);
}

int increment(int x) // definition
{
    x++; // x è locale per increment
    return x;
}