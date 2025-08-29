from typing import List

"""
Shell Sort Algorithm in Python.
Sorts a list in ascending order using shell sort.
"""


def shell_sort(array: List[int]) -> None:
    """
    Sorts the input list in ascending order using shell sort.
    Args:
        array (List[int]): List of integers to sort.
    """
    n = len(array)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2


if __name__ == "__main__":
    data = [9, 8, 3, 7, 5, 6, 4, 1]
    shell_sort(data)
    print('Sorted Array in Ascending Order:')
    print(data)
