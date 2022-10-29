# You are completely free to change this variables to check your algorithm.
num1 = -1
num2 = 28


# Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    # You need to complete this function.
    # You need to return a boolean variable . If num1 and num2 are friendly pairs return True.
    # If they are not return False.
    # The numbers must be valid according to description before determining friendly parity situations.
    # Return "Invalid" if they are not valid.

    abundancy_num1 = 0
    abundancy_num2 = 0

    # checks for the given preconditions to be natural number and different from each other
    if int(num1) != num1 or int(num2) != num2 or num1 == num2 or (num1 or num2 < 0):
        return "Invalid"

    # calculates the abundancy of number 1
    for num in range(1, num1 + 1):
        if num1 % num == 0:
            abundancy_num1 += num
    abundancy_num1 /= num1

    # calculates abundancy of number 2
    for num in range(1, num2 + 1):
        if num2 % num == 0:
            abundancy_num2 += num
    abundancy_num2 /= num2

    # returns True or False depending on the abundancies beeing equal or not / friendly pairs or not
    return abundancy_num1 == abundancy_num2


# This line prints your method's return so that you can check your output.
print(isFriendlyPair())
