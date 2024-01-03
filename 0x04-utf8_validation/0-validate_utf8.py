#!/usr/bin/python3
"""
UTF-8 validation module.
"""


def validUTF8(data):
    """
    Checks if a list of integers are valid UTF-8 codepoints.
    """
    skip = 0
    n = len(data)
    for x in range(n):
        if skip > 0:
            skip -= 1
            continue
        if type(data[x]) != int or data[x] < 0 or data[x] > 0x10ffff:
            return False
        elif data[x] <= 0x7f:
            skip = 0
        elif data[x] & 0b11111000 == 0b11110000:
            # 4-byte utf-8 character encoding
            span = 4
            if n - x >= span:
                next_body = list(map(
                    lambda i: i & 0b11000000 == 0b10000000,
                    data[x + 1: x + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[x] & 0b11110000 == 0b11100000:
            # 3-byte utf-8 character encoding
            span = 3
            if n - x >= span:
                next_body = list(map(
                    lambda i: i & 0b11000000 == 0b10000000,
                    data[x + 1: x + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[x] & 0b11100000 == 0b11000000:
            # 2-byte utf-8 character encoding
            span = 2
            if n - x >= span:
                next_body = list(map(
                    lambda i: i & 0b11000000 == 0b10000000,
                    data[x + 1: x + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        else:
            return False
    return True
