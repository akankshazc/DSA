def fib(n):
    """Calculate the nth Fibonacci number using recursion."""
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(fib(6))  # 8
    print(fib(7))  # 13
    print(fib(8))  # 21
    # Working well so far.

    # Here's is where the time complexity of O(2^n) becomes a problem:
    print(fib(50))  # 12586269025
