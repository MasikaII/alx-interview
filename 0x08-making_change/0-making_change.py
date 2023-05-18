#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    count = 0
    if total <= 0:
        return 0
    ordered = sorted(coins, reverse=True)
    for i in range(len(ordered)):
        while ordered[i] <= total:
            total = total - ordered[i]
            count += 1
    if total == 0:
        return count
    return -1
