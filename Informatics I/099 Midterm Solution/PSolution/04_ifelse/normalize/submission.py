def normalize(number, lower, upper):
    if number<lower:
        return lower
    elif number>upper:
        return upper
    else:
        return number