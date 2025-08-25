from typing import List

"""
Selection Sort Algorithm in Python.
Sorts a list in ascending order using selection sort.
"""


def selection_sort(array: List[int]) -> None:
    """
    Sorts the input list in ascending order using selection sort.
    Args:
        array (List[int]): List of integers to sort.
    """
    n = len(array)
    for step in range(n):
        min_idx = step
        for i in range(step + 1, n):
            if array[i] < array[min_idx]:
                min_idx = i
        array[step], array[min_idx] = array[min_idx], array[step]


if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    selection_sort(data)
    print('Sorted Array in Ascending Order:')
    print(data)
