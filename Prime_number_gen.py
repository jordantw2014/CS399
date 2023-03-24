"""
    Author: Jordan Wallschlaeger
    This code keeps generating prime numbers until the generator is closed.
    It can find the one millionth prime number in less than 1 minute, but can't find the 160000000th prime (takes too long.)
    Date: 01.29.2023
"""

from time import process_time


def prime_generator():
    # handle the first prime
    yield 2
    prime_cache = []  # doesn't cache 2 because we will skip even numbers anyway

    # loop over positive, odd integers
    num = 3
    while True:
        square_root = num ** 0.5

        is_prime = True

        # check to see if any existing prime number divides num
        for p in prime_cache:
            if num % p == 0:
                is_prime = False
                break
            if p > square_root:
                break
                # https://sciencing.com/calculate-coprime-6921150.html
                # If numbers have a factor pair, one of the factors must be equal to or less than the square root.
                # So, if you test all the numbers up to the square root, you can rest assured that the number is prime.

        if is_prime:
            prime_cache.append(num)
            yield num

        num += 2


# known_prime = (10, 29)
# known_prime = (1000, 7919)
# known_prime = (100000, 1299709)
known_prime = (1000000, 15485863)
# known_prime = (160000000, 3340200037)
t0 = process_time()
primes = prime_generator()
for k, prime in enumerate(primes, 1):
    if k == known_prime[0]:
        print(f"The {k:,}-th prime number is {prime}")
        assert prime == known_prime[1]
        primes.close()
print(process_time() - t0)
