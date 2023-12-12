#!/usr/bin/env python3
"""
minimim operation function
"""


def minOperations(n):
    """min operation available to n"""
    if n <= 1:
        return 0

    oper = 0
    next = 'H'
    body = 'H'

    while (len(body) < n):
        if n % len(body) == 0:
            oper += 2
            next = body
            body += body
        else:
            oper += 1
            body += next

    if len(body) != n:
        return 0

    return oper
