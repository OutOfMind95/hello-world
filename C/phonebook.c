#include <cs50.h>
#include <stdio.h>
#include <string.h>

/*int main(void)
{
    string names[] = {"Carter", "David"};
    string numbers[] = {"+1-231412-14124", "+1-124155-52352"};

    for (int i = 0; i < 2; i++)
    {
        if (strcmp(names[i], "David") == 0)
        {
            printf("Found %s\n", numbers[i]);
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;
} */

typedef struct
{
    string name;
    string number;
}
person;

int main(void)
{
    person people[2];

    people[0].name = "Carter";
    people[0].number = "+1-1414132-12313";

    people[1].name = "David";
    people[1].number = "+1-141241-13145346";

        for (int i = 0; i < 2; i++)
    {
        if (strcmp(people[i].name, "David") == 0)
        {
            printf("Found %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;
}