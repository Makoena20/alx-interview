#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    """Generate a list of booleans representing prime numbers up to max_n."""
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    
    for start in range(2, int(max_n**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, max_n + 1, start):
                sieve[multiple] = False
    
    return sieve

def count_primes_up_to(sieve, max_n):
    """Count the number of prime numbers up to each index up to max_n."""
    count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        count[i] = count[i - 1] + (1 if sieve[i] else 0)
    return count

def isWinner(x, nums):
    """Determine who wins the most rounds of the prime game."""
    if not nums or x < 1:
        return None
    
    max_n = max(nums)
    # Precompute the primes and prime counts
    sieve = sieve_of_eratosthenes(max_n)
    prime_count = count_primes_up_to(sieve, max_n)

    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        # Count how many primes are up to n
        primes_up_to_n = prime_count[n]
        if primes_up_to_n % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))


