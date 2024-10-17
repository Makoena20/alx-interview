#!/usr/bin/python3

def is_prime(num):
    """Returns True if num is a prime number, else False."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(n):
    """Counts the number of prime numbers up to n."""
    return sum(1 for i in range(1, n + 1) if is_prime(i))

def isWinner(x, nums):
    """Determines the winner of the prime game."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes(n)
        # If the number of primes is odd, Maria wins; if even, Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

