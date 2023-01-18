#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Prompt user for x
    int x = get_int ("x: ");
    // Prompt user for y
    int y = get_int ("y: ");

    //Divide x by y | e converte x e y da int a float

    float z = (float) x / (float) y;
    // ".n" Solo n cifre decimali

        printf("%.50f\n",z);
}

// float point imprecision -- superando il limite di bit utilizzabili, il calcolo risulta essere impreciso
// dividento int per int, la parte .0 viene trocata
