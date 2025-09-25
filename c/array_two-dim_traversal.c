#include <stdio.h>
#include <stdlib.h>

void traversal(char[][30], int);

void main()
{
    int i = 1, m;
    char book[10][30];

    printf("This program performs the 2-D array traversal operatoin on strings of books name!\n");
    printf("How many books in the list:");
    scanf("%d", &m);

    printf("!!Please enter the books!!\n");

    while (i <= m)
    {
        printf("Input book name (%d) in a single string:", i);
        scanf("%s", &book[i]);
        i++;
    }

    traversal(book, m);
}

void traversal(char book[][30], int n)
{
    int i = 1;
    printf("!!Entered books in the list after traversing the array are!!\n");

    while (i <= n)
    {
        printf("Books name at %d place is:", i);
        printf("%s\n", book[i]);
        i++;
    }
    printf("\n");
}