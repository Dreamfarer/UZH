In this exercise you will write a program that validates IPv4 & IPv6 addresses.

## What is an IP Address?

An [IP address](https://en.wikipedia.org/wiki/IP_address) is a unique string of characters that identifies a computing device using the Internet Protocol (IP) to communicate over a network. Your PC, your phone, your tablet, even your smart thermostat have at least one IP. There are two types of IP addresses: IPv4 & IPv6. IPv4 provides an addressing capacity of 4.3 billion addresses, while IPv6 provides an addressing capacity of 340 undecillion addresses. IPv4 is the most commonly used IP address. We are in the process of transitioning from IPv4 to IPv6.


### IPv4 Format 
IPv4 address is a string in the form `a.b.c.d` where `a`, `b`, `c`, and `d` are integers between 0 and 255. For example, `127.0.0.1` is a valid IP address, but `
300.0.0.1` is not. The IPv4 address is split into four octets by ".". Each octet is a decimal number between 0 and 255.


### IPv6 Format

 An IPv6 address is a string in the form `a:b:c:d:e:f:g:h` where `a`, `b`, `c`, `d`, `e`, `f`, `g`, and `h` are hexadecimal numbers between 0 and FFFF. For example, `2001:0db8:85a3:0000:0000:8a2e:0370:7334` is a valid IP address, but `2001:0db8:85a3:0000:0000:8a2e:0370:7334:1234` is not. The IPv6 address is split into eight hextets by ":". Each hextet is a hexadecimal number between 0 and FFFF or 0 and 65535. (Note that for this task, you can assume that IPv6 addresses always contain all eight hextets, even though according to the official specification, trailing 0000 could be omitted.)

## Task

Implement a function `is_valid_IP` that takes an arbitrary string and determines if it represents a valid IPv4 or IPv6 address. However, don't just implement everything in one function: when writing code it often makes sense to organize it into smaller parts that have only one responsibility. This makes it easier to test and debug our code. So for this exercise you will break the task into **five** functions. Read the code comments in the template in `script.py` to determine the functionality of each function and implement it accordingly.

## Hints

- First, `is_valid_IP` needs to determine if the IP address contains an IPv4 or IPv6 address. There is more than one way to detect the difference! Then, it has to call the appropriate function, either `is_valid_IPv4` or `is_valid_IPv6`, and then those functions will have to split the input string into hextets or octets and call `is_valid_IPv4_octet` or `is_valid_IPv6_hextet` respectively for each substring. This forms a function call chain.
- Each of these functions returns a boolean.
- The higher-level functions call the lower-level functions and return their return values. For example, `is_valid_IP` may return the result from callng `is_valid_IPv4`, which in turn collects the results from calling `is_valid_IPv4_octet` multiple times.
- To split a string, use the [split](https://docs.python.org/3/library/stdtypes.html#str.split) function.
- You can convert strings to integers using the [int](https://docs.python.org/3/library/functions.html#int) function. You might need this to check if the hextets/octets are in the correct range.
- To convert strings to hexadecimal numbers, you can also use the [int](https://docs.python.org/3/library/functions.html#int) function with an additional parameter that specifies the base. For example, the following code will convert the string "fe80" to the hexadecimal number 65152: `int("fe80", 16)`
- You could use Python's Regular Expression library to validate strings (but you don't have to): [re](https://docs.python.org/3/library/re.html).

