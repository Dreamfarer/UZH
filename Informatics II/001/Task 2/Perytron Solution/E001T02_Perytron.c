#include <stdio.h>
#include <stdlib.h>

#define DIMENSION 2

void printMatrix(int *matrix)
{
    printf("\n\nMatrix:\n");
    for (int i = 0; i < DIMENSION * DIMENSION; i++)
    {
        printf(" %d ", *(matrix + i));
        if ((i + 1) % DIMENSION == 0)
        {
            printf("\n");
        }
    }
}

// Get input from user and return pointer to the storage location
int *getInput()
{
    int *values = calloc(DIMENSION * DIMENSION, sizeof(int));

    printf("Chose numbers to populate a %ix%i matrix:\n", DIMENSION, DIMENSION);
    for (int i = 0; i < DIMENSION * DIMENSION; i++)
    {
        scanf("%i", &values[i]);
    }

    return values;
}

// Algorithm to implement in this excercise
int *multiply(int *matrix)
{

    int *multipliedMatrix = calloc(DIMENSION * DIMENSION, sizeof(int));
    int counter = 0;

    // Loop over all rows
    for (int row = 0; row < DIMENSION; row++)
    {
        // Loop over all columns
        for (int column = 0; column < DIMENSION; column++)
        {
            // Combine current row and line by multiplying
            int value = 0;
            for (int index = 0; index < DIMENSION; index++)
            {
                value += *(matrix + (row * DIMENSION + index)) * *(matrix + (index * DIMENSION + column));
            }
            multipliedMatrix[counter] = value;
            counter += 1;
        }
    }

    printMatrix(multipliedMatrix);
    return multipliedMatrix;
}

int main()
{
    int *matrix;
    matrix = getInput();
    printMatrix(matrix);
    multiply(matrix);
}