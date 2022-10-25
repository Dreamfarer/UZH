A friend of yours is asking for help with a task in Excel. In your friends' spreadsheet
there is a column with the header `Name`, which contains first names and
last names in each cell in two different formats. However, your friend needs the
first names and last names in two separate columns with the headers `Firstname` and
`Lastname`, respectively.

You decide to help your friend, so you need to write a function `process_data`
which reads the data from the original file `my_data.txt` and writes a file
`my_data_processed.txt` with the converted data in
comma-delimited format. In the original file
names are stored in two different formats.
- The first format can be described as `firstname<SPACE>lastname`, for example `Fred Brooks`.
- The second format looks like `lastname<SEMICOLON><SPACE>firstname`, for example `Euler; Leonhard`.

Comma-delimited means that there is a delimiter which separates the data values.
In this task the delimiter in the desired output is the _comma_ and the values separated are _firstname_
and _lastname_. If a line is empty (as in, it contains only the newline character `\n`)
in the original file, then the line in the output file should contain *only* a _comma_.
See the example below for a better understanding.

Example of an input file:

    Name
    Beat Meier

    Barbara Suter
    Berger; Roland

The corresponding output file should contain:

    Firstname,Lastname
    Beat,Meier
    ,
    Barbara,Suter
    Roland,Berger

Your function should adhere to these additional rules:
- If the input file does not exist, the function should return `False` and not write any output file.
- If the input file does exist, but is empty, an empty output file should be written.
- An input file that only contains the header (`Name`) should result in a file that contains only the
headers `Firstname,Lastname`.
- The last line of the output file should not contain the trailing newline character (`\n`).
- You can assume that the last line in the input file will never be an empty line.

**Note:** In ACCESS you will not see the output file you generate. The workspace in access is just
a starting point. During the execution of "Test & Run" or a submission, the files will only be created
temporarily, but you will not see them in ACCESS. That is why
there is a test with the name `test_print_output_file` which shows the content of 
your file generated in the testing suite. The message of this test can be found
in the "Test Output" overview after you have run "Test & Run". If your function 
does not generate a file, the message will be `No output file exists`.

**Note:** Starting with this exercise, we will provide public tests that *fail*
by default. The tests we provide will *pass* for a correct solution, but keep in
mind that the grading system runs many more exhaustive tests, so if the public
test passes, that does not necessarily mean that your solution is 100% correct,
as it might fail on certain edge or corner cases.

**Note:** The provided script defines the signature of the functions. Do not
change this signature or the automated grading will fail.

**Note:** To check for the existence of a file, you can use `import os`, followed
by a `os.path.exists(«path»)`. This snippet is already included in the template,
you just have to decide what to do in case the file does not exist.

**Hint:** The function [*find*][find] can help for this task.

[find]:https://docs.python.org/3/library/stdtypes.html#str.find
