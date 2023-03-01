#include <stdio.h>

// Algorithm to implement in this excercise
int secondLargestNumber(int *input, int size)
{
    int largestNumbers[] = {0, 0};

    for (int i = 0; i < size; i++)
    {
        if (input[i] > largestNumbers[0])
        {
            largestNumbers[1] = largestNumbers[0];
            largestNumbers[0] = input[i];
        }
        else if (input[i] > largestNumbers[1])
        {
            largestNumbers[1] = input[i];
        }
    }

    return largestNumbers[1];
}

int main()
{
    int test[] = {2, 4, 9, 7, 1};
    int arraySize = sizeof test / sizeof test[0]; // Size can only be calculated in the same scope
    int number = secondLargestNumber(test, arraySize);
    printf("%i", number);
}