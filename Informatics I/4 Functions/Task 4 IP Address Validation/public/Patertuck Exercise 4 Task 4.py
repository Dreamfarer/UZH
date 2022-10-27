#!/usr/bin/env python3

# These are examples for valid and invalid inputs to your validation function
IPv4_STRING = "127.0.0.1"
IPv4_INVALID_STRING = "300.0.0.1"
IPv6_STRING = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
IPv6_INVALID_STRING = "2001:0db8:85a3:0000:0000:8a2e:0370:7334:7334"
INVALID_IP_STRING = "Some arbitrary string"


def is_valid_IPv4_octet(octet: str):
    """Returns True if octet represents a valid IPv4 octet, False otherwise"""
    return 255 >= int(octet) >= 0


def is_valid_IPv4(ip: str):
    """Returns True if ip represents a valid IPv4 address, False otherwise"""
    for octet in ip.split("."):
        if not is_valid_IPv4_octet(octet):
            return False
    return True


def is_valid_IPv6_hextet(hextet: str):
    """Returns True if hextet represents a valid IPv6 hextet, False otherwise"""
    return 65535 >= int(hextet, 16) >= 0 and len(hextet) <= 4


def is_valid_IPv6(ip: str):
    """Returns True if ip represents a valid IPv6 address, False otherwise"""
    for hextet in ip.split(":"):
        if not is_valid_IPv6_hextet(hextet) or len(ip.split(":")) != 8:
            return False
    return True


def is_valid_IP(ip: str):
    """Returns True if ip represents a valid IPv4 or IPv6 address False otherwise"""
    if ":" in ip:
        return is_valid_IPv6(ip)
    if "." in ip:
        return is_valid_IPv4(ip)


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
