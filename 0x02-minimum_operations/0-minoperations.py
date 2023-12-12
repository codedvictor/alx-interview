#!/usr/bin/python3
"""The minimum operations coding challenge.
"""


def minOperations(n):
    """Computes the fewest number of operations needed.
    """
    if not isinstance(n, int):
        return 0
    oper_count = 0
    clip = 0
    done = 1

    while done < n:
        if clip == 0:
            clip = done
            done += clip
            oper_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clip = done
            done += clip
            oper_count += 2
        elif clip > 0:
            done += clip
            oper_count += 1
    return oper_count
