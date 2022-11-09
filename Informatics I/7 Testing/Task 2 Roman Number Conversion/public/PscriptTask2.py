#!/usr/bin/env python3

# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def convert_roman_to_int(roman):
    

    roman_single_digits = {
        # simple cases
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    roman_double_digits = {
        # compound cases
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    
    roman_double_taken = {
        "IV": False,
        "IX": False,
        "XL": False,
        "XC": False,
        "CD": False,
        "CM": False,
        
        }
    
    roman_single_count = {
        "I": 0,
        "V": 0,
        "X": 0,
        "L": 0,
        "C": 0,
        "D": 0,
        
        
        }
    
    num=0
    
    #check if all chars in roman are valid, warning 1:
    roman = str(roman)
    for i in roman:
        if not i in roman_single_digits.keys():
            raise Warning("Invalid Input - invalid char")
        if i == 'I' or i == 'X' or i =='C':
            roman_single_count[i] += 1
            if roman_single_count[i]>3:
                raise Warning("Invalid Input - too much of single char")

        elif i == 'V' or i == 'L' or i == 'D':
            roman_single_count[i] += 1
            if roman_single_count[i]>1:
                raise Warning("Invalid Input - too much of 5 char")
 
                

            

    #roman is single digits
    if roman in roman_single_digits.keys():
        return roman_single_digits[roman]
    
    
            
    #roman is a compound case   
    if roman in roman_double_digits.keys():
        return roman_double_digits[roman]
    
    #roman is add and sub
    #first get the subs in for loop
    
    cutoff = roman
    for i in roman_double_digits.keys():
        if i in roman:
            #raise warning 3 when the same double appears more than once
            if roman_double_taken[i]==True:
                raise Warning("Invalid Input - same double appears more than once")
            num += roman_double_digits[i]
            cutoff = cutoff.replace(i,'')
            roman_double_taken[i] = True #now this double is taken
            
    
    #make sure cases like "IVI","IXI", dont occur"
    for i in cutoff:
        if i=='I' and (roman_double_taken["IV"] or roman_double_taken["IX"]):
            raise Warning("Invalid Input - same chars appear before and after other chars")
        elif i=='X' and (roman_double_taken["XC"] or roman_double_taken["XL"]):
            raise Warning("Invalid Input - same chars appear before and after other chars")
        elif i=='C' and (roman_double_taken["CM"] or roman_double_taken["CD"]):
            raise Warning("Invalid Input - same chars appear before and after other chars")
    
    
    #now add the rest

    for ind,i in enumerate(cutoff):
        
        
        n=0
        #Raise exception for condition of warning 2
        if ind != len(cutoff)-1:
            n=ind+1
            if roman_single_digits[cutoff[ind]]<roman_single_digits[cutoff[n]]:
                raise Warning("Invalid Input - invalid small value before big value")
            
        
        
        
        
            
        #all good, add
        num += roman_single_digits[i]

    return num


# The following lines calls the function and prints the return
# value to the Console.
i = convert_roman_to_int("IXI")
print(i)

