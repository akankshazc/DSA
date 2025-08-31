"""
Recursive Fibonacci in Python.
Calculates the nth Fibonacci number using recursion.
"""

from typing import Any


def fib(n: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion.

    Args:
        n (int): The position in the Fibonacci sequence (1-based).

    Returns:
        int: The nth Fibonacci number.
    """
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    for i in [6, 7, 8, 50]:
        print(f"fib({i}) = {fib(i)}")
    # Note: For large n, this is very slow due to O(2^n) time complexity.
