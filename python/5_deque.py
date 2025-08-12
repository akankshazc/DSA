
"""
Deque implementation in Python.
"""

from typing import Any, List

class Deque:
    """
    A simple double-ended queue implementation.
    """
    def __init__(self) -> None:
        self.items: List[Any] = []

    def is_empty(self) -> bool:
        """Check if the deque is empty."""
        return not self.items

    def add_rear(self, item: Any) -> None:
        """Add an item to the rear of the deque."""
        self.items.append(item)

    def add_front(self, item: Any) -> None:
        """Add an item to the front of the deque."""
        self.items.insert(0, item)

    def remove_front(self) -> Any:
        """Remove and return the front item of the deque."""
        return self.items.pop(0)

    def remove_rear(self) -> Any:
        """Remove and return the rear item of the deque."""
        return self.items.pop()

    def size(self) -> int:
        """Return the number of items in the deque."""
        return len(self.items)


if __name__ == "__main__":
    d = Deque()
    print(d.is_empty())
    d.add_rear(8)
    d.add_rear(5)
    d.add_front(7)
    d.add_front(10)
    print(d.size())
    print(d.is_empty())
    d.add_rear(11)
    print(d.remove_rear())
    print(d.remove_front())
    d.add_front(55)
    d.add_rear(45)
    print(d.items)
