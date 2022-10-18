In this task, you will create a small program that helps you with keeping track of your study results. You can write down your grades into a simple text file. This text file should contain one line per course. The line starts with the name of the course (`string`), followed by your grade after a colon (`float`).

To make it easier to maintain this file, the syntax is not very strict. It should be possible to use tabs and spaces before or after the colon, to have empty lines, and to write comments by starting a line with a `#`. Please consider the following file as an example:

    # first semesters
    Informatik 1:5.75
    Informatik 2: 5.5

    # later
    Advanced Software Engineering : 6.00

Your task is to write a function `get_average_grade`. The function takes the path to such a file as the argument and reads it according to the rules mentioned before. The function should calculate the average for all the grades in the file and return it as the result. In the above example, calling the function should return `5.75`. Return `None`, if the file does not exist and `0.0` if the file does not contain any grades.

**Note:** Starting with this exercise, we will provide public tests that *fail* by default. The tests we provide will *pass* for a correct solution, but keep in mind that the grading system runs many more exhaustive tests, so if the public test passes, that does not necessarily mean that your solution is 100% correct, as it might fail on certain edge or corner cases.

**Note:** The provided script defines the signature of the functions. Do not change this signature or the automated grading will fail.

**Note:** To check for the existence of a file, you can use `import os`, followed by a `os.path.exists(«path»)`. This snippet is already included in the template, you just have to decide what to do in case the file does not exist.

