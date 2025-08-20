
"""
Python program to demonstrate working of a simple HashTable.
"""

from typing import Any, List, Tuple

hash_table: List[List[Tuple[int, Any]]] = [[] for _ in range(10)]


def check_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n in (0, 1):
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


def get_prime(n: int) -> int:
    """Get the next prime number greater than or equal to n."""
    if n % 2 == 0:
        n += 1
    while not check_prime(n):
        n += 2
    return n


def hash_function(key: int) -> int:
    """Hash function to map keys to hash table indices."""
    capacity = get_prime(10)
    return key % capacity


def insert_data(key: int, data: Any) -> None:
    """Insert or update a key-value pair in the hash table."""
    index = hash_function(key)
    for i, kv in enumerate(hash_table[index]):
        if kv[0] == key:
            hash_table[index][i] = (key, data)
            break
    else:
        hash_table[index].append((key, data))


def remove_data(key: int) -> None:
    """Remove a key-value pair from the hash table if it exists."""
    index = hash_function(key)
    for i, kv in enumerate(hash_table[index]):
        if kv[0] == key:
            del hash_table[index][i]
            break


if __name__ == "__main__":
    # Test the hash table
    insert_data(123, "apple")
    insert_data(432, "mango")
    insert_data(213, "banana")
    insert_data(654, "guava")
    insert_data(213, "orange")  # This should update the value for key 213
    print(hash_table)
    remove_data(123)
    print(hash_table)
