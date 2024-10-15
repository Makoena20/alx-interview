#!/usr/bin/python3
def isWinner(x, nums):
    if not nums or x < 1:
        return None

    def sieve_of_eratosthenes(n):
        """Returns a list of prime numbers up to n (inclusive)."""
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(2, n + 1) if sieve[i]]

    # Track the number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Precompute primes up to the maximum number in nums
    max_n = max(nums)
    primes_up_to_max = sieve_of_eratosthenes(max_n)

    for n in nums:
        primes = [p for p in primes_up_to_max if p <= n]
        moves = 0  # Number of moves taken

        # For each prime, count the moves (removing the prime and its multiples)
        while primes:
            moves += 1
            # Remove multiples of the first prime (Maria or Ben's turn)
            prime = primes[0]
            primes = [p for p in primes if p % prime != 0]

        # Maria goes first, so odd number of moves means Maria wins, even means Ben wins
        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

