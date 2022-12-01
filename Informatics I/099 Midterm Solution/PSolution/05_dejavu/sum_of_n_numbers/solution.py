#!/usr/bin/env

def sum_divisibles(limit, divisor):
    res = 0
    for n in range(limit+1):
        if n % divisor == 0:
            res += n
    return res

# examples
print( sum_divisibles(5, 2) )
print( sum_divisibles(11, 5) )
