###############################################################################
# BE AWARE THAT SOMETIMES THE SCRIPT TIMEOUTS IN ACCESS
# I don't know why, I've submitted again without changing anything and got full points
###############################################################################
def evolve(state, steps):

    # Catch wrong input
    if not isinstance(state, tuple): raise Warning("State must be of type 'tuple'")
    if not isinstance(steps, int): raise Warning("Steps must be of type 'int'")
    if len(state) == 0: raise Warning("State is empty")
    if steps <= 0: raise Warning("Steps must be greater than zero")

    stateUpdated = list(state)
    numberOfLivingCells = 0

    # Check that state is valid
    rowLength = len(state)
    columnLenght = len(state[0])

    if rowLength < 3 or columnLenght < 3: raise Warning("Board must be at least 3x3")

    for line in state:
        if not len(line) == columnLenght: raise Warning("State contains unequal line lengths")
        for char in line:
            if not char in ["-", "|", "#", " "]: raise Warning("State contains invalid characters")
    
    # Loop over each row of the field
    for rowIndex, line in enumerate(state): 
        
        # Continue if on the borders
        if rowIndex == 0 or rowIndex == len(state) - 1: continue
        
        # Loop over the whole string
        for columnIndex, char in enumerate(line):

            # Check for invalid character placement
            if rowIndex == 0 or rowIndex == len(state) -1:
                if not char == "-": raise Warning("Invalid placement of '-'")
                continue

            # Check for invalid character placement
            elif columnIndex == 0 or columnIndex == len(line) -1:
                if not char == "|": raise Warning("Invalid placement of '-'")
                continue
            
            # Check for invalid character placement
            else:
                if char in ["|", "-"]: raise Warning("Invalid placement of character inside border")
            
            # Find neighbors
            neighbors = 0 # Count neighbors
                        
            # Scan top-center neighbor
            if (rowIndex >= 2 and rowIndex <= len(state) - 2):
                if state[rowIndex - 1][columnIndex] == "#": neighbors += 1

            # Scan top-left neighbor
            if (rowIndex >= 2 and rowIndex <= len(state) - 2) and (columnIndex >= 2 and columnIndex <= len(line) - 2):
                if state[rowIndex - 1][columnIndex - 1] == "#": neighbors += 1

            # Scan top-right neighbor
            if (rowIndex >= 2 and rowIndex <= len(state) - 2) and (columnIndex >= 1 and columnIndex <= len(line) - 3):
                if state[rowIndex - 1][columnIndex + 1] == "#": neighbors += 1

            # Scan bottom-center neighbor
            if (rowIndex >= 1 and rowIndex <= len(state) - 3):
                if state[rowIndex + 1][columnIndex] == "#": neighbors += 1

            # Scan bottom-left neighbor
            if (rowIndex >= 1 and rowIndex <= len(state) - 3) and (columnIndex >= 2 and columnIndex <= len(line) - 2):
                if state[rowIndex + 1][columnIndex - 1] == "#": neighbors += 1

            # Scan bottom-right neighbor
            if (rowIndex >= 1 and rowIndex <= len(state) - 3) and (columnIndex >= 1 and columnIndex <= len(line) - 3):
                if state[rowIndex + 1][columnIndex + 1] == "#": neighbors += 1

            # Scan left neighbor
            if (columnIndex >= 2 and columnIndex <= len(line) - 2):
                if state[rowIndex][columnIndex - 1] == "#": neighbors += 1

            # Scan right neighbor
            if (columnIndex >= 1 and columnIndex <= len(line) - 3):
                if state[rowIndex][columnIndex + 1] == "#": neighbors += 1

            # print(f"row: {rowIndex}, column: {columnIndex}, neighbors: {neighbors}")

            # Check if there is a cell
            if char == "#":
                # Kill cell if it has zero, one or four or more neighbor
                if neighbors <= 1 or neighbors >= 4: 
                    stateUpdated[rowIndex] = stateUpdated[rowIndex][:columnIndex] + " " + stateUpdated[rowIndex][columnIndex+1:] 
            else:
                # Add if there are three neighbors
                if neighbors == 3: 
                    stateUpdated[rowIndex] = stateUpdated[rowIndex][:columnIndex] + "#" + stateUpdated[rowIndex][columnIndex+1:]

    # Decide wheather to call the function again or not
    if not steps == 1: stateUpdated = evolve(tuple(stateUpdated), steps - 1)[0]
    
    # Count the populated cells (#)
    for line in stateUpdated:
        for char in line:
            if char == "#": numberOfLivingCells += 1

    return tuple(stateUpdated), numberOfLivingCells # placeholder

field = (
    "--------------",
    "|            |",
    "|  ###       |",
    "|  #         |",
    "|   #        |",
    "|            |",
    "--------------"
)
steps = 4

result, alive_cells = evolve(field, steps)

print(f"Game of Life after {steps} moves:")
print(result)
print(f"{alive_cells} are alive.")

