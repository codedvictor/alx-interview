#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""

import sys


def print_stdin(dict_std, total_size):
    """
    Print stdin information
    """
    print("File size: {:d}".format(total_size))
    for key, value in sorted(dict_std.items()):
        if value != 0:
            print("{}: {:d}".format(key, value))


count = 0
code = 0
total_size = 0
dict_std = {"200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            count += 1

            if count <= 10:
                total_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in dict_std.keys()):
                    dict_std[code] += 1

            if (count == 10):
                print_stdin(dict_std, total_size)
                count = 0

finally:
    print_stdin(dict_std, total_size)
