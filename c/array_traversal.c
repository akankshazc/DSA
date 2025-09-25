#include <stdio.h>
#include <stdlib.h>

void traversal(int[], int);

void main()
{
    int i = 0, list[100], n;

    printf("This program performs the 1-D array traversal operation on numbers!\n");
    printf("How many numbers in the array:");
    scanf("%d", &n);
    printf("!!Please enter the number!!\n");
    while (i < n)
    {
        printf("Input value for the %d:", i);
        scanf("%d", &list[i]);
        i++;
    }
    traversal(list, n);
}

void traversal(int list[], int n)
{
    int i = 0;
    printf("!!Entered element in the array after traversing the array are!!\n");
    while (i < n)
    {
        printf("Element at position %d is:", i);
        printf("%d\n", list[i]);
        i++;
    }
    printf("\n");
}