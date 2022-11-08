#!/usr/bin/env python3

def evolve(state, steps):
    # implement this function
    return "", -1 # placeholder

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
print(result)
print(f"{alive_cells} are alive.")

