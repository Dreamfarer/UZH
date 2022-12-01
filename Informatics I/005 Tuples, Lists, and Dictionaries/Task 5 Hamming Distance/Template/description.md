## Definition Hamming Distance

The Hamming distance *d* of two strings of equal lengths is defined to be the number of positions at which the strings' characters differ.
This is an important concept for error detection (and correction) in data transmission.
A few examples are:

*d*("foobar", "cooler") = 3

*d*("shift", "tshif") = 5

*d*("00101", "00111") = 1

## Task

Assume you're given data by two different sensors recording the same thing. One of them stores its data as a dictionary of the form
{"times": \[<integer1>, <integer2>, <integer3>, ...\], "data": \[<string1>, <string2>, <string3>, ...\]}. The other sensor stores its recorded
data without any timestamps as a tuple of the form (<string1>, <string2>, <string3>, ...). All of the strings only contain the two characters "0" and "1". The two sensors would ideally collect the same number of datapoints
and their hamming distances should be low, but maybe your lab's equipment is a bit older and not quite that reliable. 

You will now write a function `hamming_dist` that takes one input parameter of each of these two data structures. Your function should compare the *i*-th string
of the first input to the *i*-th string of the second input, and whenever they don't match, i.e. have a Hamming distance greater than 0, you append a triplet
of the form (<string_i from first input>, <string_i from second input>, *d*(<string_i from first input>, <string_i from second input>)) to the output list.

As an example, the return value of for {"times": \[0, 2, 5\], "data": \["0010", "1101", "1100"\]} and ("0010", "1111", "0000") should be \[("1101", "1111", 1), ("1100", "0000", 2)\].
The return value of your function for two sensors sending the same strings for all timestamps should be an empty list.

If one of the Hamming distances cannot be computed because the lengths of corresponding strings differ, your function should return the string "Sensor defect detected" instead.

Perhaps, one or both sensors lost power during the recording and now you have datasets of different length or two empty datasets. In this case, your function should return the string "Empty signal on at least one of the sensors".

## Hints
- Make sure to go through all edge cases in your own testing before using a submission.
- You may write a helper function for calculating the hamming distance of two strings. However, it is essential that calling `hamming_dist` alone gives the desired return value. Otherwise you will not be awarded any points.
- Copy and paste the "sensor defect detected" and "empty signal on at least one of the sensors" returns instead of (potentially mis-)typing them to avoid wasting a submission.

