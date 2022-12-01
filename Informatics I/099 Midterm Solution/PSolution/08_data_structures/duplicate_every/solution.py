#!/usr/bin/env

def duplicate_every(l, n):
    res = []
    for i, item in enumerate(l):
        if (i+1) % n == 0:
            res.append(item)
        res.append(item)
    return res

# examples
print( duplicate_every([1, 3, 4, 5], 2) )
print( duplicate_every([1, 4, 5, 4, 3, 2, 1], 3) )
