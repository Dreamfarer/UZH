def sum_divisibles(limit, divisor):
    counter=0
    for i in range(1,limit+1):
        if i%divisor==0:
            counter += i
    
    return counter