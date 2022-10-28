#You are completely free to change this variables to check your algorithm.
num1 = 6
num2 = 28

#Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():

    # Check that the numbers are not the same and that they are natural numbers
    if not (not (num1 == num2) and (type(num1) == int) and (type(num2) == int) and (num1 > 0) and (num2 > 0)):
        return "Invalid"

    divisors_num1 = []
    divisors_num2 = []

    # Loop over every natural number up to the number itself (num1)
    for natural_number in range(num1 + 1)[1:]:

        # If we have found a divisor, add it to the list
        if num1 % natural_number == 0: divisors_num1.append(natural_number)

    # Loop over every natural number up to the number itself (num2)
    for natural_number in range(num2 + 1)[1:]:

        # If we have found a divisor, add it to the list
        if num2 % natural_number == 0: divisors_num2.append(natural_number)

    # Calulcaute abundancy of both numbers
    abundancy_num1 = sum(divisors_num1) / num1
    abundancy_num2 = sum(divisors_num2) / num2

    # Return 'True' if both numbers have the same abundancy, else return false
    if abundancy_num1 == abundancy_num2: return True
    return False

#This line prints your method's return so that you can check your output.
print(isFriendlyPair())