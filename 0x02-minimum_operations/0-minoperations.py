#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates minimum operations
    """
    if n <= 1:
        return 0
    for num in range(2, n+1):
        if n % num == 0:
            return minOperations(int(n/num)) + num
