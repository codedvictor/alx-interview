#!/usr/bin/python3
"""
A prime game module.
"""


def isWinner(x, nums):
    """
    the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    maria_wins, ben_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for p, is_prime in enumerate(primes, 1):
        if p == 1 or not is_prime:
            continue
        for q in range(p + p, n + 1, p):
            primes[q - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        ben_wins += primes_count % 2 == 0
        maria_wins += primes_count % 2 == 1
    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
