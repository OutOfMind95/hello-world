linear search -> partire da destra verso sinitra, o viceversa, e ricerco
binary search -> partire dal centro, conoscendo l ordine degli elementi

data structures -> possibilità di creare un data type unico e personale

typedef struct  // funzione per creare un data type strutturato e non semplice
{
    string x;
    string y;
}
z; // nome del data type appena creato

bubble sort
    Repeat n-1 times
        For i from 0 to n-2
            If numbers[i] and numbers[i+1] out of order
            Swap them
        If no swaps
            Quit

merge sort

    sort first half
    sort second half
merge them toghether - (first number of the first half vs first number of the second half and so on)


Recursion -> tecnica di programmazione, funzione che chiama se stessa

sistema hexadecimale -> 0 1 2 3 4 5 6 7 8 9 A B C D E F (255 max count) -> 0x ...
0x0 0x1 0x2 0x3 0x4 0x5 0x6 0x7 0x8 0x9 0xA 0xB 0xC 0xD 0xE 0xF 0x10 0x11 ... tell system to count in hexadecimal

& address the variable --> int *p = &n  *p -> con asterisco diventa un pointer

string is just a char *s --> where s points to the first character of the string

malloc -> memory allocator
free -> free memory

valgrind ./ .... -> tool per controllo bug di memoria

Queue -> specifiche proprietà, es. FIFO - first in first out
Stack -> L opposto di una queue - LIFO - last in first out