In the existing implementation, the method `word_selection` chooses `num_words` words at complete random from the word pool. This can lead to a state where almost none of the words share any letters, making it a game of pure luck, which is less fun. To make the game more entertaining, modify the game logic so that some of the chosen words tend to be more similar to each other.

Implement the method `WordLogic.is_similar(self, a, b, threshold)` which computes the similarity between `a` and `b`. It shall return `True` if the ratio is (strictly) higher than `threshold` or `False` otherwise. Use [SequenceMatcher.ratio](https://docs.python.org/3.7/library/difflib.html#difflib.SequenceMatcher.ratio) to compute the similarity.

Adjust the function `word_selection` to implement the following strategy for choosing a total of `num_words` words from the shuffled list of fixed-length words.

1. Pick one-third of `num_words` at random. Use [floor](https://docs.python.org/3.7/library/math.html#math.floor) to handle cases in which `num_words` is not dividable by `3`.
2. For the remaining words:
    * Randomly pick one of the already selected words by using [choice](https://docs.python.org/3/library/random.html#random.choice).
    * Randomly pick a word from the remaining word pool. Add it to the list of selected words if `compute_similarity` confirms more than 40% similarity.
    * Repeat until enough sufficiently similar words have been found. You can assume that it is always possible to find such a word and you do not need to prevent endless loops.

**Note:** Instead of repeatedly performing a random selection, you can also [shuffle](https://docs.python.org/3/library/random.html#random.shuffle) a list once and then just iterate over all elements or slice the list to get a random subset.

**Note:** The list returned by `word_selection` may not contain any duplicates

**Note:** Make sure that your implementation is fast, especially the word selection. If the execution takes longer than 3s, it will be terminated and you will see a crash report in the solution hint.

**Note:** All state must be contained within the class. Do not store information in global variables or in class variables. It must be possible to use multiple instances of the classes in parallel without suffering from side effects.

**Note:** Do not change provided function signatures or the automated grading will fail.

**Note:** We strongly encourage you to add more tests to the public test suite.

