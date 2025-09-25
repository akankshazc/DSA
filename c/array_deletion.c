#include <stdio.h>
#include <stdlib.h>

int deletion(int[], int, int);
void display(int[], int);

void main()
{
    int i = 0, list[100], n, position;

    printf("This program performs the 1-D array deltion operation on numbers!\n");
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

    printf("Enter the position from where we want to delete a number:");
    scanf("%d", &position);

    display(list, n);
}

void display(int list[], int n)
{
    int i = 0;

    printf("!!Entered elements in the array are!!\n");

    while (i < n)
    {
        printf("Element at position %d is:", i);
        printf("%d\n", list[i]);
        i++;
    }

    printf("\n");
}

int deletion(int list[], int n, int position)
{
    int i, item;
    i = n;
    item - list[position];

    printf("Deleted item form the position %d is: %d\n", position, item);

    while (position <= n)
    {
        list[position] = list[position + 1];
        position++;
    }
    n = n - 1;
    return n;
}