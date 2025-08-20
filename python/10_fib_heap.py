
"""
Fibonacci Heap implementation in Python.
"""

import math
from typing import List, Optional


class FibonacciTree:
    """
    A tree node in the Fibonacci heap.
    """

    def __init__(self, value: int) -> None:
        """Initialize a Fibonacci tree node."""
        self.value: int = value
        self.child: List['FibonacciTree'] = []
        self.order: int = 0

    def add_at_end(self, t: 'FibonacciTree') -> None:
        """Add a tree as a child to this node."""
        self.child.append(t)
        self.order += 1


class FibonacciHeap:
    """
    A simple Fibonacci heap implementation.
    """

    def __init__(self) -> None:
        """Initialize an empty Fibonacci heap."""
        self.trees: List[FibonacciTree] = []
        self.least: Optional[FibonacciTree] = None
        self.count: int = 0

    def insert_node(self, value: int) -> None:
        """Insert a node with the given value into the heap."""
        new_tree = FibonacciTree(value)
        self.trees.append(new_tree)
        if self.least is None or value < self.least.value:
            self.least = new_tree
        self.count += 1

    def get_min(self) -> Optional[int]:
        """Get the minimum value in the heap."""
        if self.least is None:
            return None
        return self.least.value

    def extract_min(self) -> Optional[int]:
        """Extract and return the minimum value from the heap."""
        smallest = self.least
        if smallest is not None:
            for child in smallest.child:
                self.trees.append(child)
            self.trees.remove(smallest)
            if not self.trees:
                self.least = None
            else:
                self.least = self.trees[0]
                self.consolidate()
            self.count -= 1
            return smallest.value
        return None

    def consolidate(self) -> None:
        """Consolidate the trees in the heap to maintain the heap property."""
        aux: List[Optional[FibonacciTree]] = [
            None] * (floor_log(self.count) + 1)
        while self.trees:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.value > y.value:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order += 1
            aux[order] = x
        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if self.least is None or k.value < self.least.value:
                    self.least = k


def floor_log(x: int) -> int:
    """Return the floor of log2(x)."""
    return math.frexp(x)[1] - 1


if __name__ == "__main__":
    fibonacci_heap = FibonacciHeap()
    fibonacci_heap.insert_node(7)
    fibonacci_heap.insert_node(3)
    fibonacci_heap.insert_node(17)
    fibonacci_heap.insert_node(24)
    print(
        f"The minimum value of the fibonacci heap: {fibonacci_heap.get_min()}")
    print(f"The minimum value removed: {fibonacci_heap.extract_min()}")
