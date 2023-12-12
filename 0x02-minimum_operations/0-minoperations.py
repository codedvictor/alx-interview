#!/usr/bin/env python3
"""
minimim operation function
"""


def minOperations(n):
    if n <= 1:
        return 0

    oper = 0
    div = 2

    while n > 1:
        while n % div == 0:
            oper += div
            n //= div
        div += 1

    return oper

if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
