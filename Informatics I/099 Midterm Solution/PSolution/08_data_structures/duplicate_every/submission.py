def duplicate_every(l, n):
    res=[]
    for i in l:
        if l.index(i)%n==n-1:
            res.append(i)
            res.append(i)
        else:
            res.append(i)
    return res