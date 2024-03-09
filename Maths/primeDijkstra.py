# Most of the code is generated by AI. Still, the idea is the same.
from time import perf_counter
import math

def generate_primes_trial_division(limit):
    primes = []

    for num in range(2, limit + 1):
        if is_prime_trial_division(num):
            primes.append(num)

    return primes

def is_prime_trial_division(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False

    return True

def prime_dijkstra_approach(range_end):
    is_prime = [True] * (range_end + 1)
    primes = [2]
    multiples = [4]

    for i in range(3, range_end, 2):  # Skip even numbers
        if is_prime[i]:
            primes.append(i)
            multiples.append(i * i)

            # Mark multiples as non-prime
            for j in range(i * i, range_end + 1, 2 * i):  # Skip even multiples
                is_prime[j] = False

    return primes

# Set the value of x
x = 1050000

# Run the function with memory profiling
t1 = perf_counter()
prime_dijkstra_approach(x)
t2 = perf_counter()
t3 = perf_counter()
generate_primes_trial_division(x)
t4 = perf_counter()
print(f'Elapsed time (Dijkstra): {t2 - t1} seconds.')
print(f'Elapsed {t4 - t3} seconds')