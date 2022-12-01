# You can freely adopt these values to try your solution
# with different values.
plain_text = "abzAZ!"
shift_by = -1


def rot_n():
    encoded = ""
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = lower_alphabet.upper()
    for char in plain_text:

        if char in lower_alphabet:
            # this utilizes a neat trick with the modulo operator.
            # since we only want letters within the alphabet, we take
            # the rest of the shifted character.

            # ┌──────────────────────────────────────┐
            # │EXAMPLE                               │
            # ├──────────────────────────────────────┤
            # │shift_by = 5                          │
            # │char     = w                          │
            # │lower_alphabet.index(char) = 22       │
            # │22+5=27                               │
            # │27%26=1                               │
            # │lower_alphabet[1]="b"                 │
            # ├──────────────────────────────────────┤
            # │This also handles negative shifts!    │
            # │-1 % 26 = 25                          │
            # ├──────────────────────────────────────┤
            # │IMPORTANT                             │
            # │z is index 25. We divide by 26 so that│
            # │z+1=0->"a"                            │
            # └──────────────────────────────────────┘
            index = (lower_alphabet.index(char) + shift_by) % 26
            encoded += lower_alphabet[index]
            continue

        elif char in upper_alphabet:
            # same principle as above
            index = (upper_alphabet.index(char) + shift_by) % 26
            encoded += upper_alphabet[index]
            continue

        # character is neither in upper or lower alphabet. We move on.
        encoded += char

    # You don't need to change the following line.
    # It simply returns the string created above.
    return encoded


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(rot_n())
