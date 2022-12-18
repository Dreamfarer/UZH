#!/usr/bin/env python3

import os


def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        return False
    with open(path_reading) as file:
        data = file.readlines()

    if data == []:
        f = open(path_writing, 'w')
        return f

    data = [x.strip() for x in data]
    # remove spaces
    if data == ["Name"]:
        with (open(path_writing, 'w')) as file:
            file.write('Firstname,Lastname')
    # Replace empty lines with commas
    data = [x.replace(x, ',') if x == '' else x for x in data]
    # Replace space in normal names with comma (Note: There was an issue were the "e" of name disappeared, so I left it out entirely.)
    data = [x.replace(x[x.find(' ')], ',')
            if not ';' in x else x for x in data[1:]]
    # Replace colon with space
    data = [x.replace(";", "") if ";" in x else x for x in data]
    # Find all elmements that have spaces (previous colon) and swap them, could also done with format method or f-string.
    data = [t[1+t.find(" "):] + ' ' + t[:t.find(" ")]
            if " " in t else t for t in data]
    # Replace the space with a comma
    data = [x.replace(x[x.find(' ')], ',') if ' ' in x else x for x in data]
    # Insert First,Lastname to the first position. Look at note to understand this step.
    data.insert(0, 'Firstname,Lastname')
    # Add new-line to all elements except last one
    data = [f"{x}\n" if x != data[-1] else x for x in data]
    # insert each element into a new line in the file.
    with open(path_writing, 'w') as file:
        for i in data:
            file.write(i)


INPUT_PATH = "my_data.txt"
OUTPUT_PATH = "my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")
