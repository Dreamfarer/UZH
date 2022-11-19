#!/usr/bin/env python3

class MagicDrawingBoard:

    def __init__(self, x, y):
        self.__size = [x, y]
        self.reset() # Image gets initialized here
        
        # Check drawing board size
        try: 
            if x < 1 or y < 1: raise Warning("Drawing board too small")
        except: raise Warning("Wrong drawing board format")

    # Draw pixel
    def pixel(self, coordinates):
        try: 
            if coordinates[0] < 0 or coordinates[1] < 0: raise Warning("Pixel out of bounds")
            self.__image[coordinates[1]][coordinates[0]] = "1"
        except: raise Warning("Pixel out of bounds")

    # Draw rectangle
    def rect(self, coordinates_start, coordinates_right_bottom):
        
        # Calculate how many pxiels to the right and to the bottom need to be drawn
        try:
            x = coordinates_right_bottom[0] - 1 - coordinates_start[0]
            y = coordinates_right_bottom[1] - 1 - coordinates_start[1]
        except: raise Warning("Wrong coordinate format")

        # Check that the rectangle is "positive"
        if x < 0 or y < 0 or coordinates_start[0] < 0 or coordinates_start[1] < 0 or coordinates_right_bottom[0] < 0 or coordinates_right_bottom[1] < 0: raise Warning("False rectangle notation")

        # Paint each pixel on its own (raise warning if the rectangle is too large for the drawing board)
        try:
            for index_y in range(y+1):
                for index_x in range(x+1):
                    # print("y: " + str(coordinates_start[1] + index_y) + ", x: " + str(coordinates_start[0] + index_x))
                    self.__image[coordinates_start[1] + index_y][coordinates_start[0] + index_x] = "1"
        except: raise Warning("Pixel out of bounds")

    # Reset the image
    def reset(self):
        self.__image = [] # Holds the image
        row = []
        # Create reference row and populate every column with it
        for not_important in range(self.__size[0]): row.append("0")
        for not_important in range(self.__size[1]): self.__image.append(row.copy())
    
    # Return the image
    def img(self):
        output = ""
        for row in self.__image:
            output += "".join(row) + "\n"
        return output[:-1]

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    db = MagicDrawingBoard(6,4) # instantiation of a specific size
    db.pixel((2,1)) # draw at one coordinate
    db.rect((2,2), (5,4)) # draw a rectangle
    img = db.img() # return the drawn image
    print(img)
    db.reset() # reset the field again
