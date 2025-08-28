from typing import List

"""
Radix Sort Algorithm in Python.
Sorts a list in ascending order using radix sort and counting sort for each digit place.
"""


def counting_sort(array: List[int], place: int) -> None:
    """
    Performs counting sort on the input list based on the digit at the given place.
    Args:
        array (List[int]): List of integers to sort.
        place (int): Digit place to sort by.
    """
    size = len(array)
    output = [0] * size
    count = [0] * 10
    for i in range(size):
        index = array[i] // place
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(size):
        array[i] = output[i]


def radix_sort(array: List[int]) -> None:
    """
    Sorts the input list in ascending order using radix sort.
    Args:
        array (List[int]): List of integers to sort.
    """
    if not array:
        return
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        counting_sort(array, place)
        place *= 10


if __name__ == "__main__":
    data = [121, 432, 564, 23, 1, 45, 788]
    radix_sort(data)
    print(data)
