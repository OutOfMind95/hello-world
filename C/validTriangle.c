#include <stdio.h>
#include <cs50.h>

int main(void)
{
bool valid_triangle(float x, float y, float z);
{

    if (x <= 0 || y <= 0 || z <= 0)
    {
        return false;
    }
    if ((x+y) <= z || (x+z) <= y || (z+y) <= x)
    {
        return false;
    }
    else
    {
        return true;
    }
}
}