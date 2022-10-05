A password should contain a variety of characters to make it harder
to guess. You are part of a team that develops a new application,
which requires passwords to satisfy the following rules:

* Has a length of 8-16 chars.
* Only contains the characters a-z, A-Z, digits, or the special chars "+", "-", "*", "/".
* Must contain at least 2 lower case and 2 upper case characters, 2 digits, and 2 special chars.

Implement a checker that decides whether a given password candidate
is valid. The password candidate will be given to you in a variable
`pwd`. 

Write a program that checks whether `pwd` satisfies all rules. The validity of the password should be verified by a function called `is_valid` and your task is to complete the function.

Please make sure that your solution is self-contained within the `is_valid` function. That is, only change the body of the function, not the code outside the function. Your function is expected to return the validity in a bool value.

While working on this task, these utilities will make your life easier: 
* Use [*isupper*][isupper]/[*islower*][islower] to decide whether a string is upper case or lower case (e.g., `"A".isupper()` is `True`).
* Use [*isdigit*][isdigit] to check if it is a number (e.g., `"3".isdigit()` is `True`).
* Use the [`in`][in_operator] operator to check whether a specific character exists in a string (e.g., `"a" in "abc"` is `True`).

PS: As a sidenote, it should be mentioned that this is only a programming example. In the real world, password rules like these have limited effectiveness, especially considering that they increase the likelyhood of people just putting their password on a post-it next to the screen. A simple sentence like "i prefer tea over coffee every time" is likely more secure than "Paj1vae0j!bo" and easier to remember. Never implement password rules like this in a real application. [Optional](https://blog.codinghorror.com/password-rules-are-bullshit/) [reading](https://xkcd.com/936/)

[isupper]: https://docs.python.org/3/library/stdtypes.html#str.isupper
[islower]: https://docs.python.org/3/library/stdtypes.html#str.islower
[isdigit]: https://docs.python.org/3/library/stdtypes.html#str.isdigit
[in_operator]: https://docs.python.org/3/reference/expressions.html#membership-test-operations

