When Romeo and Juliet first met, it was love at first sight.
Because of their feuding families they got to know each other hidden from any hateful eyes.
As they didn't think about anything else, they even forgot to exchange numbers in due time.
Only when Tybalt - Juliets cousin who is especially at odds with Romeo's family, appears on scene,
Juliet hastily hacks a few of her digits into Romeo's phone and whispers him to text her on Whatsapp and leaves.

Later that day, Romeo looks at the newly saved contact and checks whether the number is on Whatsapp.
Unfortunately it is not! He realizes that one digit seems to be missing.
What a pain! Juliet only entered `076432165`!

He comes to you with a bleeding heart and complains about his fate.
But then you have a brilliant idea to help him!
Fortunately you have heard about that new feature which shows you whether
a given number is linked on Whatsapp or not.

You hatch a plan to simply figure out all possible combinations producing valid phone numbers by adding a digit to the incomplete number `076432165` and then checking if they are registered in Whatsapp.

## Task - Repeting for loops, indices and most common list operations
Your job in this task is to help Romeo by writing a program that produces all possibilities
of phone numbers and provides him a list of possble numbers that are linked on Whatsapp.
For this you may adhere to the following specification:
- Valid numbers have 10 digits in total and start with 07
- `get_possible_nrs(n)` accepts a number string `n` where one digit is missing
- `n` may be assumed to start with `07` and then contain 7 further digits (in total 9, i.e. one missing digit).
- `get_possible_nrs(n)` returns a list of whatsapp number strings that might belong to juliet.
- A number that may belong to juliet contains exactly one digit more than `n` (10 digits).
- The single missing digit may be assumed to be at any index after the starting `07` within `n`.
- Make sure your returned list does not contain duplicates.
- `wa_nrs` is a list of numbers that are registered with Whatsapp.
- Compare your generated numbers with the numbers in `wa_nrs` to return only those from your function which exist in Whatsapp.

## Hints
- visualize where/at what indices a single digit could be inserted in a given test number
- Think of which python constructs you need to populate a list and check for list inclusion

**Note:** The provided script defines the signature of the function. Do not change this signature or the automated grading will fail. Do not use any global variables (except reading `wa_nrs`). Your solution should be self-contained in the solution function.

