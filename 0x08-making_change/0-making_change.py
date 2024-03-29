#!/usr/bin/python3
"""
Change making module.
"""


def makeChange(coins, total):
    """
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    ream = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while ream > 0:
        if coin_idx >= n:
            return -1
        if ream - sorted_coins[coin_idx] >= 0:
            ream -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
