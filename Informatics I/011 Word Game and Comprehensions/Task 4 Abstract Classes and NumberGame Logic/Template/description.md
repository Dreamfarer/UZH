The current version of the game uses words as secrets. Through the power of inheritance, we will extend the game with a new game logic that uses numbers as secrets. In this task, you will perform the required "refactorings" in the code base.

First of all, create an *abstract* `GameLogic` class. Remember that abstract classes need to extend `ABC` and annotate all their abstract methods with `@abstractmethod`. Move the current constructor (`__init__`) and the `check` method from `WordLogic` to `GameLogic`. The content is not specific to `WordLogic` and can be re-used. `GameLogic` should introduce two *abstract* methods `_word_selection` and `_generate_feedback`, which should have a *protected* visibility, the former should be used in the constructor, the latter in the `check` method.

Now, adjust the `WordLogic` class to inherit the base functionality from `GameLogic` and to make it instantiable by implementing the abstract methods. To make the current `WordLogic` implementation compatible, you also need to adjust the visibilities of the existing methods.

Finally, create the new class `NumberLogic` that extends `GameLogic` and works as follows:

* On initialization, it generates string sequences of numbers (e.g., for `len_words=4` examples would be `"1234"`, `"5291"`, `"5930"`, ...). These sequences may only contain each specific number exactly once. As a result, `"0000"` would be an invalid number, because 0 is contained multiple times.
* The same rules of `WordLogic` apply as well. The logic should generate `num_words` candidate sequences that all have a length of `len_words` digits. Both are stored as public variables in the base class and can therefore be directly accessed.
* One of the generated sequences is randomly picked as the secret and the goal is to guess the secret.
* The player can add guesses by calling the `GameLogic.check` function. As long as attempts are left, the system will return feedback through the `NumberLogic._generate_feedback` method that describes how close the guess is to the secret.
* In contrast to `WordGame`, the numbers are NOT compared index-by-index, the system will only say how many numbers from the guess also appear in the secret. For example, if the secret is `"1063"`, a guess `"1234"` would get the feedback `"2/4 correct"`, because both contain the numbers 1 and 3. While a guess `"3601"` would get the feedback `"4/4 correct"`, it is still not the accepted solution due to the wrong number order.
* `NumberLogic` should override the `check` method and reject guesses that contain repeated numbers or have the wrong length by raising a `Warning`. If a guess is valid, the call should be delegated to the super class.

**Note:** The list returned by `word_selection` may not contain any duplicates

**Note:** Let both `NumberLogic` and `WordLogic` inherit from `GameLogic`. Both subclasses must *not* specify their own constructors: it must only exist in the abstract `GameLogic` class. Likewise, `WordLogic` should *not* implement `check`, and `NumberLogic`'s override of `check` must only extend the `check` function to reject guesses (calling `check` in the super class eventually), not duplicate it entirely.

**Note:** All state must be contained within the class. Do not store information in global variables or in class variables. It must be possible to use multiple instances of the classes in parallel without suffering from side effects.

**Note:** Do not change provided function signatures or the automated grading will fail. Also make sure that you declare all classes in the corresponding files.

**Note:** We strongly encourage you to add more tests to the public test suite.

