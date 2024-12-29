"""
Processing recursive number lists
"""

from functools import lru_cache
import time

def r_sum(nested_sum_list):
    """Sum all the numbers of a nested list"""
    tot = 0
    for element in nested_sum_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot


def r_max(nxs):
    """
    Find the maximum in a recursive structure of lists within other lists
    Precondition: No lists or sublists are empty
    """
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e
        if first_time or val > largest:
            largest = val
            first_time = False
    return largest

"""
- Memoization
The following two functions are used to calculate the nth Fibonacci number using memoization.
The first function uses a dictionary to store the computed values, while the second function uses the lru_cache decorator.
The lru_cache decorator is a built-in Python decorator that caches the results of the function calls.
"""

def fib(n, memo={}):
    """Return the nth Fibonacci number using memoization"""

    # Check if the input is a positive integer
    if type(n) != int or n < 0:
        raise ValueError("Input must be a positive integer")

    # If we have cached the value; then return it
    if n in memo:
        return memo[n]

    # Compute the nth term
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]

@lru_cache(maxsize=None)
def fibonacci(n):
    """Return the nth Fibonacci number using a simple recursive approach"""

    # Check if the input is a positive integer
    if type(n) != int or n < 0:
        raise ValueError("Input must be a positive integer")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# for n in range(1, 10):
#     print(n, ":", fib(n))

# for n in range(1, 1000):
#     print(n, ":", fibonacci(n))

t0 = time.process_time()
n = 35
result = fib(n)
t1 = time.process_time()
print("fib({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))

t0 = time.process_time()
n = 35
result = fibonacci(n)
t1 = time.process_time()
print("fibonacci({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))

# print(r_sum([1, 2, [3, 4], [5, 6, [7, 8]]]))
# print(r_max([2, 9, [1, 13], 8, 6]))
# print(r_max(["joe", ["sam", "ben"]]))
