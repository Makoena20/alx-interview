#!/usr/bin/python3
"""
Prime Game Module
"""


def isWinner(x, nums):
    """
    Determines the winner of a prime game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the numbers in each round.

    Returns:
        str: The name of the player who won the most rounds.
            If it's a tie, return None.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False

    # Sieve of Eratosthenes to find all prime numbers up to max_num
    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Calculate the number of primes less than or equal to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0
    for num in nums:
        if prime_count[num] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

