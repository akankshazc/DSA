
"""
Max-Heap data structure in Python.
"""

from typing import List


def heapify(arr: List[int], n: int, i: int) -> None:
    """
    Heapify subtree rooted at index i in array arr of size n.
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def insert(array: List[int], new_num: int) -> None:
    """
    Insert a new number into the max-heap.
    """
    array.append(new_num)
    current = len(array) - 1
    while current > 0:
        parent = (current - 1) // 2
        if array[current] > array[parent]:
            array[current], array[parent] = array[parent], array[current]
            current = parent
        else:
            break


def delete_node(array: List[int], num: int) -> None:
    """
    Delete a number from the max-heap.
    """
    size = len(array)
    for i in range(size):
        if array[i] == num:
            break
    else:
        return  # Element not found
    array[i], array[-1] = array[-1], array[i]
    array.pop()  # Remove the last element which is now the number to be deleted
    if i < len(array):
        heapify(array, len(array), i)


if __name__ == "__main__":
    arr: List[int] = []
    insert(arr, 3)
    insert(arr, 4)
    insert(arr, 9)
    insert(arr, 5)
    insert(arr, 2)
    print("Max-Heap array:", arr)
    delete_node(arr, 4)
    print("After deleting an element:", arr)
