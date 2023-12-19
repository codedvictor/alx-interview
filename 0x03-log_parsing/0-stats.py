#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""

import sys


def print_stdin(dic, size):
    """
    Print stdin information
    """
    print("File size: {:d}".format(size))
    for x in sorted(dic.keys()):
        if dic[x] != 0:
            print("{}: {:d}".format(x, dic[x]))


stdin = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_stdin(stdin, size)

        std_list = line.split()
        count += 1

        try:
            size += int(std_list[-1])
        except:
            pass

        try:
            if std_list[-2] in stdin:
                stdin[std_list[-2]] += 1
        except:
            pass
    print_stdin(stdin, size)


except KeyboardInterrupt:
    print_stdin(stdin, size)
    raise
