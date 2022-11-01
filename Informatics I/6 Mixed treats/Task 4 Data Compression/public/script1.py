#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def compress(data):
    
    #if data is empty, return empty tuple, empty list
    if data == []:
        return tuple((),[])
    
    #if the data contains empty dictionary, return empty tuple, list of empty dict
    if data[0]=={}:
        return tuple((),[()])
    
    res_list = []
    
    for current_dict in data:
        
        current_keys = list(current_dict.keys()) #list of keys
        current_keys.sort()
        
        #go thru current keys, put the values in a list in an ordered manner
        current_values_sorted = []
        
        for i in current_keys:
            current_values_sorted.append(current_dict[i])
        
        #add sorted values to the return list as tuple
        res_list.append(tuple(current_values_sorted))
        
        
    #take keys of the first dict(since all dict have same keys),
    #sort it, convert to tuple     
    res_tuple = tuple(sorted(data[0].keys()))  
    return res_tuple, res_list
    
    


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
data = [
    {}
]
print(compress(data))