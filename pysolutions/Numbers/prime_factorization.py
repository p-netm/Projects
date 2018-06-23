""" Have the user enter a number and find all Prime Factors (if there are any) and display them """
import math

number = int(input("Enter a prime number(whole number, decimals will be truncated to whole numbers): "))
def find_prime(number):
    # we get the factors and then determine which of them are prime
    factor = 2
    factor_set = set()
    while factor <= number:
        if number % factor == 0:
            number = number // factor
            # we check if the factor is prime
            if is_prime(factor):
                factor_set.add(factor)
        else:
            factor += 1
    return factor_set

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i =i + 6
    return True

prime_factors = find_prime(number)
if len(prime_factors) == 0:
    print("No prime Factors found")
else:
    print("Found " + str(len(prime_factors)) + " prime factors: " , prime_factors)

def test_function():
    assert find_prime(147) == { 3, 7}
    assert find_prime(2) == {2}
    assert find_prime(1) == set()
    assert find_prime(3) == {3}
    assert find_prime(0) == set()
    assert find_prime(330) == {2, 3, 5, 11}

test_function()