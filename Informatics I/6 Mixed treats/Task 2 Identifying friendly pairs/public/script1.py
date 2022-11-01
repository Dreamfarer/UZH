#You are completely free to change this variables to check your algorithm.
num1 = 6 
num2 = 0

#Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    #You need to complete this function.
    #You need to return a boolean variable . If num1 and num2 are friendly pairs return True. 
    # If they are not return False. 
    # The numbers must be valid according to description before determining friendly parity situations. 
    # Return "Invalid" if they are not valid.
    
    
    #Catch some errors
    if type(num1) != int or type(num2)!=int:
        return "Invalid"
   
    if num1 == num2:
        return "Invalid"
    
    if num1<=0 or num2<=0:
        return "Invalid"
    
    
    
    list1=[]
    list2=[]
    
    #get all divisors of num1 to list1
    for i in range(1,num1+1):
        if num1%i==0:
            list1.append(i)
    #get all divisors of num2 to list2        
    for i in range(1,num2+1):
        if num2%i==0:
            list2.append(i)
    print(list1)
    print(list2)
    
    #calculate ro(num) - abundancy
    sum1 = 0
    sum2 = 0
    for i in list1:
        sum1+=i
    for i in list2:
        sum2 += i
    print(sum1*num2)
    print(sum2*num1)
    
    if sum1 * num2 == sum2 * num1:
        return True
    else:
        return False
    

#This line prints your method's return so that you can check your output.
print(isFriendlyPair())