
#!/usr/bin/env python3


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def min_domino_rotations(top, bottom):
    is_possible = False
    # we can't create equal rows unless all dominos share the same value.
    # therefore, we take one domino's two numbers and check if they are in
    # every other domino.
    first_domino = (top[0], bottom[0])

    bottom_missing = 0
    top_missing = 0
    for num in first_domino:
        # since we checked the first domino, we start from index 1
        for i in range(1, len(top)):
            # neither number
            if num != top[i] and num != bottom[i]:
                break
            # check which side of the domino is holding the number
            # -> see how many are missing
            elif num != top[i]:
                top_missing += 1
            elif num != bottom[i]:
                bottom_missing += 1
        # for ... else only executes the "else" block if the for loop
        # hasn't been broken. In our context, it means that all dominos
        # have the current number either in the top or bottom row.
        else:
            is_possible = True
            break

    # Now we either know if it's possible or impossible.
    if not is_possible:
        return -1
    # We have top_missing and bottom_missing now due to the previous loop.
    # Since they indicate how many non-nums are missing, they also refer
    # to the minimum steps we need to complete the row.
    # We take the smaller of the two.

    return min(top_missing, bottom_missing)


# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))
