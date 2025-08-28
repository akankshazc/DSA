"""
Counting Sort Algorithm in Python.
Sorts a list in ascending order using counting sort.
"""

from typing import List


def counting_sort(array: List[int]) -> None:
    """
    Sorts the input list in ascending order using counting sort.
    Args:
        array (List[int]): List of non-negative integers to sort.
    """
    size = len(array)
    output = [0] * size
    count = [0] * (max(array) + 1)
    for i in range(size):
        count[array[i]] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
    for i in range(size):
        array[i] = output[i]


if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1]
    counting_sort(data)
    print("Sorted Array in Ascending Order:")
    print(data)
