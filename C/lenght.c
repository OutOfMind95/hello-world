#include <stdio.h>
#include <cs50.h>
#include <string.h> // aggiunge la funzione strlen


/*{
    string name = get_string("Name: ");

    int i = 0;
    while (name[i] != '\0')
    {
        i++;
    }
    printf("%i\n", i);
}*/

int main(void)
{
    string name = get_string("Name: ");

    int lenght = strlen(name);

    printf("%i\n", lenght);
}