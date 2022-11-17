In this task, you will implement a [magic drawing board](https://en.wikipedia.org/wiki/Magna_Doodle). In the physical world, you can use a magnetic pen to draw on the board and move the lever from one side of the board to the other to clear the board and start over. In contrast to the board that you probably had as a kid, this time, you will draw with method calls. For example:

    db = MagicDrawingBoard(6,4) # instantiation of a specific size
    db.pixel((1,1)) # draw at one coordinate
    db.rect((2,2), (5,4)) # draw a rectangle
    img = db.img() # return the drawn image
    db.reset() # reset the field again

You implementation should have two methods to draw on the board. `pixel` just fills the pixel at the x/y tuple that is provided as the argument. `rect` fills a rectangle that is spanned by the two x/y coordinate tuples. The rectangle must be "positive", i.e., the end coordinates must be to the lower right of the start coordinates. The end coordinates should also be "exclusive", meaning that the second coordinate indicates the first pixel that won't be drawn anymore (e.g., `pixel((0,0))` is the same as `rect((0,0), (1,1))` ). A call to `reset` should clear the entire board. The board size itself is provided in the constructor.

You implementation should handle invalid situations by raising a `Warning`. Examples are out-of-bounds coordinates, rectangles for which the end coordinate is smaller than the start coordinate in either dimension, or if an invalid size is provided for the board (i.e., x or y are smaller than 1). 

If you run the example from before, `img` should contain a string in the following format:

    "000000\n
    010000\n
    001110\n
    001110"

Obviously, it is very inconvenient to store the drawing board as a string internally, because it makes it hard to change the values. The great thing is, using a class allows you to hide your implementation details. Internally, you can model your board in any way you like. You just generate the string on the fly when it is requested. Make sure though that you do not expose any instance variables to the outside.

**Note:** You do not have to validate that the parameters are actually tuples.

**Note:** All state must be contained within the class. Do not store information in global variables or in class variables. It has to be possible to use multiple instances of the classes in parallel without suffering from side effects.

**Note:** The provided files define the signatures of various classes and functions. Do not change these signatures or the automated grading will fail.

**Note:** We strongly encourage you to add more tests to the public test suite.