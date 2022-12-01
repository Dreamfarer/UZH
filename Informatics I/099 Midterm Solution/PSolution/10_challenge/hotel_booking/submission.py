def booking(pricing, products):
    total=0
    discount=0
    freepark=0
    orders={}
    breakfastfree=0
    roomcount=0
    tenoff=False
    roomprice=0
    
    for item in products:
        total += pricing[item]
        if item == "standard" or item == "executive" or item == "suite":
            roomcount+=1
            roomprice+=pricing[item]
        
        if not item in orders:
            orders[item] =0
        orders[item] += 1
        
    
    for item in orders.keys():
        if item == "executive":
            freepark += orders["executive"]
        if item == "suite":
            freepark += orders["suite"]
            breakfastfree += orders["suite"]
        
        
    if roomcount >=3:
        tenoff=True
    
    #calculate discount
    if tenoff:
        discount += 0.1*roomprice
    
    if "parking" in orders.keys():
        discount += min(freepark,orders["parking"])*pricing["parking"]
    if "breakfast" in orders.keys():
        discount += min(breakfastfree,orders["breakfast"])*pricing["breakfast"]

    
    return total,discount,total-discount