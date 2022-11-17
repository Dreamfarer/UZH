In this task, you will implement a `ProfanityFilter` class that can be used to redact swear words in messages. Please see the following example that illustrates all relevant functions.

    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg) # abc defghi ?#$?#$? jklmno

The filter gets initialized with a list of offensive keywords and a replacement template. Every occurence of any of these words should be replaced with a string that is generated from the template. If the word size is shorter than the template, a substring should be used that starts from the beginning, for longer sizes, the template should be repeated as often as necessary. The implementation also has to be case-insensitive, so regardless of how the keywords are defined or in which form they appear in the text, they should get replaced.

The keywords can be provided in any order and might contain each other as subwords. The profanity filter has to properly replace every word though, so make sure to sort the list of offensive words by size and replace larger words first to avoid a subword-only replacement. Make sure that you also replace offensive words that only occur as a subword (e.g. "fishotter" should become "fi?#$?ter").

You can implement the class the way you like. Apart from the signature of constructor and `filter` no requirements will be enforced. We encourage you to use utility functions in the class, but this is up to you. You could, for example, create a private function `__clean` that generates an escaped sequence for a provided word of an arbitrary length (e.g., in the example `clean("batch")` == "?#$?#").

**Note:** You can use the function `str.replace` to make the replacement easier and `sorted`/`reversed` to help you with the sorting.

**Note:** All state must be contained within the class. Do not store information in global variables or in class variables. It must be possible to use multiple instances of the classes in parallel without suffering from side effects.

**Note:** The provided files define the signatures of various classes and functions. Do not change these signatures or the automated grading will fail.

**Note:** We strongly encourage you to add more tests to the public test suite.