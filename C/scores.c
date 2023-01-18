#include <stdio.h>
#include <cs50.h>

/*int main(void)
{
    int score1 = 72;
    int score2 = 73;
    int score3 = 33;

    printf("Average: %f\n", (score1 + score2 + score3) / 3.0);
}*/

/*int main(void)
{
    int scores[3]; //quante variabili voglio inserire nell'array

    scores[0] = get_int("Scores: "); //parto da 0, index

    scores[1] = get_int("Scores: "); // in questo modo posso inserire qualunque numero

    scores[2] = get_int("Scores: ");

        printf("Average: %f\n", (scores[0] + scores[1] + scores [2]) / 3.0); // ulizzo adesso una sola variabile
}*/

int main(void)
{
    int n = get_int("How many scores? ");

    int scores[n];

    for (int i = 0; i < n; i++)
    {
        scores[i] = get_int("Scores: ");
    }
        printf("Average: %f\n", (scores[0] + scores[1] + scores [2]) / 3.0);
}