In this exercise, you will implement a version of [John Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). Read the Wikipedia page to understand what it's about.

For this implementation, we assume a *finite*, two-dimensional, rectangular game world represented as follows:
 * Each cell in the world is represented by a single character. Cells are either populated (with an octothrope, `#`) or unpopulated (with an empty space).
 * Each cell has exactly eight neighbors (2 horizontally, 2 vertically, and 4 diagonally), except at the corners and edges where cells have only 3 or 5 neighbors respectively.
 * To make the visualization of a game world easier, we surround it by a frame that is 1 character wide all around: the frame consists of hyphens (`-`) at the top and bottom and of vertical bars (`|`) on the left and right side of the world.
 * The smallest possible world contains a single cell (3x3 including the frame).

Here is an example of a 12x5 world of the Game of Life (14x7 including the frame), where five cells are populated:

```plain
    --------------
    |            |
    |  ###       |
    |  #         |
    |   #        |
    |            |
    --------------
```

We now want to let this world go to the next step of the Game of Life. For this, every cell gets updated simultaneously according to the following rules:

 * A cell that is populated and has only one or no populated neighbors dies of solitude and becomes unpopulated.
 * A cell that is populated and has four or more populated neighbors dies due to overpopulation and becomes unpopulated.
 * A cell that is populated and has two or three populated neighbors survives and stays populated.
 * A cell that is unpopulated and has exactly three populated neighbor cells gets born and becomes populated.
 * All other cells remain unpopulated.
 * For cells next to the frame, frame cells are considered unpopulated from the cell's perspective.

The following illustrates these rules for four steps in time. Try covering the subsequent steps and predict which cells will be populated to get used to how the game works.

```plain
    --------------      --------------      --------------      --------------      --------------
    |            |      |   #        |      |  ##        |      |  ##        |      | ###        |
    |  ###       |      |  ##        |      |  # #       |      | ##         |      | #          |
    |  #         |  --> |  # #       | -->  |  #         | -->  |   #        | -->  |  #         |
    |   #        |      |            |      |            |      |            |      |            |
    |            |      |            |      |            |      |            |      |            |
    --------------      --------------      --------------      --------------      --------------
```

To encode such a world in Python data types you already know, we will be using tuples of strings:

```python
    world = (
        "--------------",
        "|            |",
        "|   ###      |",
        "|   #        |",
        "|    #       |",
        "|            |",
        "--------------"
    )
```

Your task is to implement and test a function `evolve` that takes two arguments: 1) a game world and 2) an integer number indicating how many evolutionary steps should be performed. The return value of the function should be a tuple of two values: the game world after the final step and the number of populated cells.

For example, a call to `evolve(world, 4)` using the `world` above should return the following result:

```python
    result = (
        "--------------",
        "| ###        |",
        "| #          |",
        "|  #         |",
        "|            |",
        "|            |",
        "--------------"
    ), 5)
```

The function should check that the input parameters are of the correct types and valid according to the requirements:

 * The provided game world is valid if:
   * ... it only contains the defined characters ("-", "|", "#", " ") and only at the right positions as described above.
   * ... each line has the same length.
   * ... it has a sensible size (both dimensions of the world including the frame are greater than 2 - otherwise there would be no game cells).
 * The provided number of evolutionary steps is a positive integer.

Any invalid call to `evolve` should `raise` a `Warning`.
A good implementation should also include an appropriate error message to elaborate the `Warning` (e.g., `raise Warning("invalid character in world: $")`), but the automated grading will not take this into consideration.
Make sure that your test suite checks whether an exception is raised for all kinds of invalid calls!
Various ways exist to do so, make yourself familiar with `self.assertRaises` to learn about the most convenient one.

You're best off implementing this task using **test-driven development**: Implement the test suite (`public/tests.py`) first. Consider, in detail, how `evolve` should behave. What should be the output given various valid worlds as input? Which kinds of calls should raise a `Warning`? Once you've implemented a comprehensive test suite, implement the function itself.

Both the test suite (in `public/tests.py`) and the corresponding function (in `public/script.py`) will be considered for the grading. The test suite will be graded based on its ability to correctly identify correct and incorrect implementations and the function itself will be graded based on its correctness.

**Note:** The test suite must only test the function `evolve` directly, even if you decide to factor out functionality into utility functions in your own implementation.

**Note:** This is a complex programming task. Think about how the task could be split into multiple sub-tasks and solve the problem by combining these smaller functions.

**Note:** The provided files define the signatures of various classes and functions. Do not change these signatures or the automated grading will fail.

**Note:** Both the test suite (`public/tests.py`) and the function (`public/script.py`) should be submitted for grading. Don't submit until you've implemented both. Don't forget either of them.

**Note:** Remember that the names of test functions must start with `test`.

