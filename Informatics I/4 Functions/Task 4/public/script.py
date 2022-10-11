#!/usr/bin/env python3

# These are examples for valid and invalid inputs to your validation function
IPv4_STRING = "127.0.0.1"
IPv4_INVALID_STRING = "300.0.0.1"
IPv6_STRING = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
IPv6_INVALID_STRING = "2001:0db8:85a3:0000:0000:8a2e:0370:7334:7334"
INVALID_IP_STRING = "Some arbitrary string"

##############################################################################
# !ATTENTION!
# This solution only gives 2 out of 3 points. Reason is the following:
# "Invalid IPv6 address falsely identified as valid"
# DO NOT SUBMIT IT
##############################################################################

def is_valid_IPv4_octet(octet: str):
    """Returns True if octet represents a valid IPv4 octet, False otherwise"""

    string_octet = octet # Store a copy to compare it later on

    # Check that there are less or equal than 3 characters
    if len(octet) > 3: return False 
    
    # Try to convert the provided octet into an integer, if it fails, it is not a valid octet
    try: octet = int(octet)
    except: return False

    # Prevent cases like "000" = "0", because "127.000.0.1" is illegal
    if not str(octet) == string_octet: return False

    # Check that the octet is not bigger than 255
    if octet > 255: return False 
    else: return True

def is_valid_IPv4(ip: str):
    """Returns True if ip represents a valid IPv4 address, False otherwise"""
    
    # Check if the structure is correct for IPv4
    if ip.count(".") == 3:
        octets = ip.split(".") # Split the string into substrings

        # Loop over every octet and validate it
        for octet in octets:
            if not is_valid_IPv4_octet(octet): return False
        return True
            
def is_valid_IPv6_hextet(hextet: str):
    """Returns True if hextet represents a valid IPv6 hextet, False otherwise"""

    # Check that there are less or equal than 4 characters
    if len(hextet) > 4: return False
    
    # Try to convert the provided hextet into an integer, if it fails, it is not a valid hextet
    try: hextet = int(hextet, 16)
    except: return False

    # Check that hextet is not bigger than 65535
    if hextet > 65535: return False 
    else: return True

def is_valid_IPv6(ip: str):
    """Returns True if ip represents a valid IPv6 address, False otherwise"""
    
    # Check if the structure is correct for IPv6
    if ip.count(":") == 7:
        hextets = ip.split(":") # Split the string into substrings

        # Loop over every hextet and validate it
        for hextet in hextets:
            if not is_valid_IPv6_hextet(hextet): return False
        return True

def is_valid_IP(ip: str):
    """Returns True if ip represents a valid IPv4 or IPv6 address False otherwise"""

    # Call functions which check whether the provided ip adress is a valid IPv4 or IPv6 adress
    if is_valid_IPv4(ip) or is_valid_IPv6(ip):
        return True
    else:
        return False

# The following lines call is_valid_IP and print the result.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(
    f"{IPv4_STRING} is a valid IP Address:",
    is_valid_IP(IPv4_STRING))
print(
    f"{IPv4_INVALID_STRING} is a valid IP Address:",
    is_valid_IP(IPv4_INVALID_STRING),
)
print(
    f"{IPv6_STRING} is a valid IP Address:",
    is_valid_IP(IPv6_STRING))
print(
    f"{IPv6_INVALID_STRING} is a valid IP Address:",
    is_valid_IP(IPv6_INVALID_STRING),
)
print(
    f"{INVALID_IP_STRING} is a valid IP Address:",
    is_valid_IP(INVALID_IP_STRING),
)
