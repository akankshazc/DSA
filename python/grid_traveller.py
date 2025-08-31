"""
Grid Traveller in Python.
Calculates the number of ways to travel in an m x n grid moving only down or right.
"""

from typing import Any


def grid_traveller(m: int, n: int) -> int:
    """
    Returns the number of ways to travel in an m x n grid moving only down or right.
    Args:
        m (int): Number of rows.
        n (int): Number of columns.
    Returns:
        int: Number of possible paths.
    """
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveller(m - 1, n) + grid_traveller(m, n - 1)


if __name__ == "__main__":
    for m, n in [(1, 1), (2, 3), (3, 2), (3, 3), (18, 18)]:
        print(f"grid_traveller({m}, {n}) = {grid_traveller(m, n)}")
