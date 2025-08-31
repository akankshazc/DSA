"""
Memoized Recursive Fibonacci in Python.
Calculates the nth Fibonacci number using recursion with memoization.
"""

from typing import Dict


def fib(n: int, memo: Dict[int, int] = None) -> int:
    """
    Calculate the nth Fibonacci number using recursion with memoization.

    Args:
        n (int): The position in the Fibonacci sequence (1-based).
        memo (Dict[int, int], optional): Dictionary for memoization.

    Returns:
        int: The nth Fibonacci number.
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    for i in [6, 7, 8, 50]:
        print(f"fib({i}) = {fib(i)}")
    # Efficient for large n.
