#include <cs50.h>
#include <stdio.h>
#include <string.h>

/*int main(void)
{
    int numbers[] = {4, 6, 8, 2, 7, 5, 0}; //creo un array vuoto e definisco il contenuto con {}

    for (int i = 0; i < 7; i++)
    {
        if (numbers[i] == -1)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;
} */

int main(void)
{
    string names [] = {"Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"};

    for (int i = 0; i < 7; i++)
    {
        if (strcmp(names[i], "Ron") == 0) // per le strings bisogna utilizzare la funzione strcmp (compara le stringhe)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;
}