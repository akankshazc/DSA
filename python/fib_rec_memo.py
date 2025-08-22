def fib(n, memo={}):
    """Calculate the nth Fibonacci number using recursion with memoization."""
    if n in memo.keys():
        return memo[n]
    if n == 1 or n == 2:
        return 1
    memo[n] = fib(n-1, memo=memo) + fib(n-2, memo=memo)
    return memo[n]


if __name__ == "__main__":
    print(fib(6))  # 8
    print(fib(7))  # 13
    print(fib(8))  # 21
    # Working well so far.

    # This works well for higher values of n too.
    # The time complexity is O(n) (just like the space complexity.)
    print(fib(50))  # 12586269025
