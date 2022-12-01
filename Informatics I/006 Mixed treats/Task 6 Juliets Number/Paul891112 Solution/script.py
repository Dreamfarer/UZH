#!/usr/bin/env python3

# use this list of presumably known Whatsapp numbers to check
# whether a trial nr from the function below exists in Whatsapp.
# Note that the grading framework might use different numbers here.
wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]


# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def get_possible_nrs(n):
    # This function accepts a string n for juliets number where one digit is missing.
    # and should return a list of all whatsapp numbers that might belong to juliet 
    possible_nrs_for_juliet = []
    return_list=[]
    
    for i in range(1,9):
        for j in range(0,10):
            poss = n[0:i+1]+"{}".format(j)+n[i+1:]
            if poss in possible_nrs_for_juliet:
                continue
            else:
                possible_nrs_for_juliet.append(poss)
            
    for wa_nr in wa_nrs:
        for possible in possible_nrs_for_juliet:
            if wa_nr == possible:
                return_list.append(wa_nr)
    # Don't forget to return your 
    return return_list

# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("076432165"))
