h = 5

def build_string_pyramid():

    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    
    s = "1"

    if h  == 0:
        return s
    if h == 1:
        s = "1"
        return s
    else:  
        #part one of pyramid
        for i in range(2,h+1):
            s = s + "\n" + "1"
        
            for j in range (2,i+1):
                s = s + "*" +str(j)
        
        #part two: reverse pyramid

        for i in range (h,1,-1):
            s = s + "\n" + "1"
            
            for j in range (2,i):
                s = s + "*" + str(j)


        
        
        

    return s
            
print(build_string_pyramid())
