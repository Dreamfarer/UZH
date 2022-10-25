In number theory, a friendly number is a **natural number** that shares a certain characteristic called _abundancy_ with one or more other numbers. Abundancy is the ratio between the sum of divisors of the number and the number itself. Two **different** numbers with the **same abundancy** form a **friendly pair.**

The abundancy of n is the rational number σ(n) / n, in which σ denotes the _sum of divisors function_. A number n is a friendly number if there exists m ≠ n where σ(m) / m = σ(n) / n.

For example 6 is a friendly number because abundancy of 6 and 28 are same : 2. Thus 6 and 28 are friendly pair

- The divisors of 6 are 1, 2, 3, 6. σ(n) is calculated as the sum of divisors.
- So in this case σ(6) = 1+2+3+6 = 12. We found σ(6) = 12. Now we need to calculate the abundancy of 6.
- The abundancy is σ(n) / n . So in this case: σ(6) / 6 = 12 / 6 = 2
- So the abundancy of 6 is 2.
- Now we calculate the abundancy of 28: σ(28) / 28 = (1+2+4+7+14+28) / 28 = 2.
- Since abundancies of 6 and 28 are both 2 we call (6, 28) a friendly pair.

Your task is to implement an algorithm in the function `isFriendlyPair` which checks whether two numbers are a friendly pair or not.

Please make sure that your solution is self-contained within the `isFriendlyPair` function. That is, write your code inside of the function not outside of it. You are free to change initial numbers to test your outcome but make sure you don't write code outside of the function and that you don't change the name of the function. Your function is expected to return `True` if the given numbers are a friendly pair and `False` if they are not. If the numbers do not comply with required preconditions (being natural and different from each other), your implementation should return the string `"Invalid"`.

- _Hint 1: Try to understand the problem first. Use pen and paper to break down the problem. Coding will be a lot easier if you are able to solve the problem on paper first and determine the steps on paper._
- _Hint 2: Please make sure the function returns the correct types._

[More Information about friendly pairs](https://sites.google.com/site/mathematicsmiscellany/very-special-numbers)
