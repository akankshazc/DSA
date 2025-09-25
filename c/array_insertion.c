#include <stdio.h>
#include <stdlib.h>

int insertion(int[], int, int, int);
void display(int[], int);

void main()
{
    int i = 0, list[100], n, position, item;

    printf("This program performs 1-D array insertion operation on numbers!\n");
    printf("How many numbers are there in the array:");
    scanf("%d", &n);
    printf("!!Please enter the number!!\n");

    while (i < n)
    {
        printf("Input value for the %d:", i);
        scanf("%d", &list[i]);
        i++;
    }
    display(list, n);
    printf("Enter the position where we want to add a new number:");
    scanf("%d", &item);

    n = insertion(list, n, position, item);

    display(list, n);
}

void display(int list[], int n)
{
    int i = 0;
    printf("!!Entered elements int he array are!!\n");

    while (i < n)
    {
        printf("Element at position %d is:", i);
        printf("%d\n", list[i]);
        i++;
    }

    printf("\n");
}

int insertion(int list[], int n, int position, int item)
{
    int i;
    i = n;
    while (i > position)
    {
        list[i + 1] = list[i];
        i--;
    }
    list[position] = item;
    n = n + 1;
    return n;
}