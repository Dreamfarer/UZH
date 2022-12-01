# You are completely free to change this variables to check your algorithm.
num1 = 4999
num2 = 14326


def isFriendlyPair():

    abundancy_1 = 0
    abundancy_2 = 0

    if num1 == num2 or not isinstance(num1, int) or not isinstance(num2, int) or num1 <= 0 or num2 <= 0:
        return "Invalid"

    for i in range(1, int(num1 ** 0.5) + 1):
        if num1 % i == 0:
            abundancy_1 += i + (num1/i if num1/i != i else 0)

    for i in range(1, int(num2 ** 0.5) + 1):
        if num2 % i == 0:
            abundancy_2 += i + (num2/i if num2/i != i else 0)

    if abundancy_1 / num1 == abundancy_2 / num2:
        return True

    return False


# This line prints your method's return so that you can check your output.
print(isFriendlyPair())
