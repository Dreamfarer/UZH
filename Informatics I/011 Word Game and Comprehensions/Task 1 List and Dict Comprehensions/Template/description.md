In this task, you will practice list and dict comprehensions

You can find 6 functions in `script.py`. The first one has already been implemented as an example. The others are for you to finish. The import at the beginning simply provides the word list from `resource/words.txt` as a list.

As a general rule, all functions *must* start with a `return` statement and they *must* return either a list or a dict comprehension. The first function is provided as an example. The only exemption to this rule is `alphabet()`.

`words_containing_string(s)` should return a list of all those words from `words` which contain the given string `s`.

`words_starting_with_character(c)` should return a list of all those words from `words` which start the given character `c`.

`alphabet()` should return a string containing the 26 lower-case latin characters `a` through `z`. This function is exempt from the rule above. However, you may *not* use the literal string `"abcdefghijklmnopqrstuvwxyz"` anywhere in your solution! There are other ways of obtaining the alphabet in python - please refer to the internet search engine of your choice.

`dictionary()` should return a dictionary where each key-value pair consists of a letter of the alphabet and a list of all the words starting with the corresponding character. So for example `dictionary()["a"]` should contain the list of all words starting with "a". You can use both the `alphabet()` and `words_starting_with_character(c)` functions to your advantage.

`censored_words(s)` receives *one string* `s`. Calling the function should return a copy of the `words` list, in which all words that contain `s` should be converted to a string of the same length that only contains lower-case "x" chars. For example, calling `censored_words("bad")` would return a list of all words, but the words "badly", "badge" and "barbados" would have been changed to "xxxxx", "xxxxx" and "xxxxxxxx", respectively.

**Note:** Do not change provided function signatures or the automated grading will fail.

**Note:** We strongly encourage you to add more tests to the public test suite.

