#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    counter = 0
    if sum <= 0:
        return 0
    sort = sorted(coins, reverse=True)
    for i in range(len(sort)):
        while sort[i] <= sum:
            sum = sum - sort[i]
            counter += 1
    if sum == 0:
        return counter
    return -1
