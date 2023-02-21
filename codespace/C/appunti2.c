Function -> set di input con un output
prima di tutto bisogna dichiarare la funzione - return-type name(argument-list);
return-type - il tipo di output che si desidera, ad esempio int
name - il nome della funzione
argument-list - una lista separata da , con il set di input da inserire nella funzione

                int add_two_int(int a, int b);

                float mult_two_float(float a, float b)
                    {
                        float product = a * b;          Una volta dichiarata la funzione bisogna definire il codice
                        return product;
                    }
oppure
                float mult_two_float(float a, float b)
                    {
                        return = a * b;
                    }

Call function -> es. int z = add_two_int(a, b);

Variable Scope - Local Variable (accesso solo dove sono create) and Global Variable (utilizzabili ovunque)

int main(void)
{
    int result = triple(5); // local variable
}
int triple(int x)
{
    return x * 3;
}

#include <stdio.h>

float global = 0.5050 // global variable - dichiarata prima della funzione

int main(void)
{
    triple();
    printf("%f\n", global)
}

/* void triple(void)
{
    global *=3;
} */

Local Variable - non hanno effetto se non dove sono dichiarate

int increment(int x); // declaration

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