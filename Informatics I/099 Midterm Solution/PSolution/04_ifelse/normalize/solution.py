#!/usr/bin/env

def normalize(number, lower, upper):
    if number > upper:
        return upper
    elif number < lower:
        return lower
    return number

    # or:
    #return min(upper, max(lower, number))

# examples
print( normalize(1.5, 0, 1) )
print( normalize(15, 10, 20) )
