"""
Quick Sort Algorithm in Python.
Sorts a list in ascending order using quicksort.
"""

from typing import List


def partition(array: List[int], low: int, high: int) -> int:
    """
    Finds the partition position for quicksort.
    Args:
        array (List[int]): List of integers to sort.
        low (int): Starting index.
        high (int): Ending index.
    Returns:
        int: Partition index.
    """
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array: List[int], low: int, high: int) -> None:
    """
    Sorts the input list in ascending order using quicksort.
    Args:
        array (List[int]): List of integers to sort.
        low (int): Starting index.
        high (int): Ending index.
    """
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


if __name__ == "__main__":
    data = [8, 7, 2, 1, 0, 9, 6]
    print("Unsorted Array")
    print(data)
    size = len(data)
    quick_sort(data, 0, size - 1)
    print('Sorted Array in Ascending Order:')
    print(data)
