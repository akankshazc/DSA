
"""
Bucket Sort Algorithm in Python.
Sorts a list of floating point numbers in [0, 1) using bucket sort.
"""

from typing import List


def bucket_sort(array: List[float]) -> List[float]:
    """
    Sorts the input list of floats in ascending order using bucket sort.
    Args:
        array (List[float]): List of floats in [0, 1) to sort.
    Returns:
        List[float]: Sorted list.
    """
    n = len(array)
    buckets: List[List[float]] = [[] for _ in range(n)]
    for value in array:
        index = int(n * value)
        buckets[index].append(value)
    for i in range(n):
        buckets[i].sort()
    k = 0
    for i in range(n):
        for value in buckets[i]:
            array[k] = value
            k += 1
    return array


if __name__ == "__main__":
    array = [.42, .32, .33, .52, .37, .47, .51]
    print("Sorted Array in ascending order is")
    print(bucket_sort(array))
