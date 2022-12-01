#!/usr/bin/env python3

def evolve(world, steps):
    # different cases to raise Errors for wrong inputs
    if type(world) != tuple or type(steps) != int:
        raise Warning("The input-type is wrong!")

    if world == ():
        raise Warning("The world is empty!")

    if steps < 1:
        raise Warning("The steps needs to be a positive integer!")

    for l in world:
        if type(l) != str:
            raise Warning("A line in the input-world is not a string!")

    for l in world[0]:
        if l != "-":
            raise Warning("Your first line doesn't consist only of - !")

    if not any("-" in l for l in world):
        raise Warning("The world-input is invalid!")

    if not any("|" in l for l in world):
        raise Warning("The world-input is invalid!")

    for l in world[-1]:
        if l != "-":
            raise Warning("Your last line doesn't consist only of - !")

    length_world = len(world[0])
    if length_world <= 2:
        raise Warning("The input-world needs to be at least 2 characters long!")
    for l in world[1:]:
        if len(l) != length_world:
            raise Warning("The lines in the input-world don't have the same length!")

    for l in world[1:-1]:
        if l[0] != "|" or l[-1] != "|":
            raise Warning("Every line in the input-world needs to start and end with a | !")

    # implement this function
    count = 0
    duplicate = world

    # takes the different lines without the "-" line above and below
    for line_count, line in enumerate(duplicate[1:-1]):

        # takes the different symbols from the line without the "|"
        for index, symbol in enumerate(line[1:-1]):

            if not (symbol == " " or symbol == "#"):
                raise Warning("Every column needs to start or end with a - !")

            # counts the amount of "#" in the neighboring fields
            count = 0
            count += world[line_count].count("#", index, index + 3)
            count += (world[line_count + 1][index] + world[line_count + 1][index + 2]).count("#")
            count += world[line_count + 2].count("#", index, index + 3)

            # different adaptions for different counts of "#" and state of field itself
            if symbol == "#":
                if count <= 1:
                    line = "".join(line[:index + 1] + " " + line[index + 2:])
                if count >= 4:
                    line = "".join(line[:index + 1] + " " + line[index + 2:])
            if symbol == " " and count == 3:
                line = "".join(line[:index + 1] + "#" + line[index + 2:])

        # replaces the old line with the new line
        y = list(duplicate)
        y[line_count + 1] = line
        duplicate = tuple(y)

    # calls the function again if there are more steps
    if steps != 1:
        steps -= 1
        duplicate = evolve(duplicate, steps)[0]

    # counts the number of # in the tuple
    for l in duplicate:
        count += l.count("#")

    return duplicate, count


field = (
    "--------------",
    "|            |",
    "|   ###      |",
    "|   #        |",
    "|    #       |",
    "|            |",
    "--------------"
)
steps = 4

result, alive_cells = evolve(field, steps)

print(f"Game of Life after {steps} moves:")
for row in result:
    print(row)
print(f"{alive_cells} are alive.")
