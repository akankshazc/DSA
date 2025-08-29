
"""
Heap Sort Algorithm in Python.
Sorts a list in ascending order using heap sort.
"""

from typing import List


def heapify(arr: List[int], n: int, i: int) -> None:
    """
    Maintains the max-heap property for a subtree rooted at index i.
    Args:
        arr (List[int]): List of integers to heapify.
        n (int): Size of the heap.
        i (int): Root index of the subtree.
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: List[int]) -> None:
    """
    Sorts the input list in ascending order using heap sort.
    Args:
        arr (List[int]): List of integers to sort.
    """
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == "__main__":
    arr = [1, 12, 9, 5, 6, 10]
    heap_sort(arr)
    print("Sorted array is")
    print(' '.join(str(x) for x in arr))
