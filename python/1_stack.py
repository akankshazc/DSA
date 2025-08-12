
"""
Stack implementation in Python using a class.
"""

from typing import Any, List


class Stack:
    """A simple stack implementation."""

    def __init__(self) -> None:
        self._items: List[Any] = []

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return not self._items

    def push(self, item: Any) -> None:
        """Push an item onto the stack."""
        self._items.append(item)

    def pop(self) -> Any:
        """Pop an item from the stack. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def __repr__(self) -> str:
        return f"Stack({self._items})"


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack contents:", stack)
    try:
        popped = stack.pop()
        print(f"Popped from stack: {popped}")
    except IndexError as e:
        print(e)
    print("Stack after popping an element:", stack)
