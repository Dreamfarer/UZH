#!/usr/bin/env

def add(n):
    def f(x):
        return n + x
    return f

    # or
    #return lambda x: n + x

# examples
print( add(3)(10) )
print( add(-5)(15) )
