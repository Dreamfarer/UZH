num1 = 6
num2 = 28


def isFriendlyPair():

    # Checks if the inputs are int and postive, or equal
    if type(num1) != int or type(num2) != int or num1 == num2 or num1 <= 0 or num2 <= 0:
        return "Invalid"

    # Calculates divisors using prime factors, no clue how it works, got it from here:
    # https://stackoverflow.com/questions/70635382/fastest-way-to-produce-a-list-of-all-divisors-of-a-number
    def getDivs(N):
        factors = {1}
        maxP = int(N ** 0.5)
        p, inc = 2, 1
        while p <= maxP:
            while N % p == 0:
                factors.update([f * p for f in factors])
                N //= p
                maxP = int(N ** 0.5)
            p, inc = p + inc, 2
        if N > 1:
            factors.update([f * N for f in factors])
        return sum(factors)

    # Calculates & Compares abundance
    if getDivs(num1)/num1 == getDivs(num2)/num2:
        return True
    return False


print(isFriendlyPair())
