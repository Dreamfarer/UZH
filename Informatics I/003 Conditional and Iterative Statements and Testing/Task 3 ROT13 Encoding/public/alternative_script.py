# ultra short solution using smort maffs

plain_text = "a, B, z#!"
shift_by = 1


def rot_n():
    encoded = ""

    for char in plain_text:
        if char.isalpha():
            if char.islower():
                encoded += chr((ord(char) + shift_by - 123) % 26 + 97)
            else:
                encoded += chr((ord(char) + shift_by - 91) % 26 + 65)
        else:
            encoded += char

    return encoded


print(rot_n())
