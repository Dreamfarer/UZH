#!/usr/bin/env python3
# This is the previous implementation, which contains several mistakes.
# Instead of fixing the implementation, provide tests that isolate and
# illustrate the issues. You don't have to fix this implementation.
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def median(numbers):
    # sort list
    numbers = sorted(numbers)
    # select element "in the middle"
    middle_idx = len(numbers) // 2
    # case distinction
    if len(numbers) % 2:
        return int(numbers[middle_idx])
    else:
        l = numbers[middle_idx-1]
        r = numbers[middle_idx]
        return int((l+r)//2)
