
"""
Priority Queue (Max-Heap) implementation in Python.
"""

from typing import List

def heapify(arr: List[int], n: int, i: int) -> None:
    """
    Heapify subtree rooted at index i in array arr of size n.
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

def insert(array: List[int], newNum: int) -> None:
    """
    Insert a new number into the heap.
    """
    size = len(array)
    array.append(newNum)
    for i in range((size // 2) - 1, -1, -1):
        heapify(array, size, i)

def deleteNode(array: List[int], num: int) -> None:
    """
    Delete a number from the heap.
    """
    size = len(array)
    for i in range(size):
        if num == array[i]:
            break
    else:
        return  # Element not found
    array[i], array[size - 1] = array[size - 1], array[i]
    array.pop()
    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)


if __name__ == "__main__":
    arr: List[int] = []
    insert(arr, 3)
    insert(arr, 4)
    insert(arr, 9)
    insert(arr, 5)
    insert(arr, 2)
    print(f"Max-Heap array: {arr}")
    deleteNode(arr, 4)
    print(f"After deleting an element: {arr}")
