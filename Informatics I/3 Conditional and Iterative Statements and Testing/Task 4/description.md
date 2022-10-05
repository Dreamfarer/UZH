# Sieve of Eratosthenes

A prime number is a natural number greater than 1, whose only factors are 1 and itself.
To find out whether a number *n* is prime, one has to test whether any of the integers up to the squareroot of *n* divide *n*.
If none of them do, then *n* is prime.

For big prime numbers this factorization is computationally expensive, which makes prime numbers especially interesting for cryptography.
Thus, a vast variety of algorithms and optimizations for factorizing big numbers (and therefore testing whether they are prime) exists nowadays.

However, even ancient Greek mathematicians were already fascinated by prime numbers.
One method, the Sieve of Eratosthenes, as devised by Eratosthenes of Cyrene dates back to the third century BCE.
It can be used for finding all smaller primes and is still comparably efficient up to this date.
The method starts with a list of all the integers from 2 up to a desired limit.
Then, the first unmarked number is marked as prime and all of its multiples get crossed off the list.
This step is repeated iteratively until all numbers are either marked as prime or crossed off (once a number bigger than the squareroot of the biggest integer on the list is marked as prime, one can already stop the iterative steps and simply mark all remaining integers as prime).


Write a program that implements the Sieve of Eratosthenes algorithm to return a (sorted) list of all primes <= n.


Please make sure that your solution is self-contained within the `sieve_of_eratosthenes()` function. That is, only change the body of the function, not the code outside the function.
Your function is expected to return a list that contains all primes (and no other integers) up to n.
If there is no prime up to *n*, your function should return \["empty"\] instead of an empty list.

## Hints

- Beware of modifying lists that are you are currently looping over. This can lead to skipped elements, for instance non-primes that remain in the list your function returns.
- Your implementation should be close to the Sieve of Eratosthenes algorithm, but you may use contains(), remove() etc. on lists which might slow your implementation down.
- Use math.sqrt() and math.ceil() to find the last integer you need to *sieve*.