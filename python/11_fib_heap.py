
"""
Fibonacci Heap implementation in Python.
"""

import math
from typing import List, Optional

class FibonacciTree:
    """
    A tree node in the Fibonacci heap.
    """
    def __init__(self, key: float) -> None:
        """Initialize a Fibonacci tree node."""
        self.key: float = key
        self.children: List['FibonacciTree'] = []
        self.parent: Optional['FibonacciTree'] = None
        self.marked: bool = False
        self.order: int = 0

    def add_at_end(self, t: 'FibonacciTree') -> None:
        """Add a tree as a child to this node."""
        self.children.append(t)
        t.parent = self
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

    def insert(self, key: float) -> None:
        """Insert a node with the given key into the heap."""
        new_tree = FibonacciTree(key)
        self.trees.append(new_tree)
        if self.least is None or key < self.least.key:
            self.least = new_tree
        self.count += 1

    def get_min(self) -> Optional[float]:
        """Get the minimum key in the heap."""
        if self.least is None:
            return None
        return self.least.key

    def extract_min(self) -> Optional[float]:
        """Extract and return the minimum key from the heap."""
        smallest = self.least
        if smallest is not None:
            for child in smallest.children:
                child.parent = None
                self.trees.append(child)
            self.trees.remove(smallest)
            if not self.trees:
                self.least = None
            else:
                self.least = self.trees[0]
                self.consolidate()
            self.count -= 1
            return smallest.key
        return None

    def consolidate(self) -> None:
        """Consolidate the trees in the heap to maintain the heap property."""
        aux: List[Optional[FibonacciTree]] = [None] * (floor_log2(self.count) + 1)
        while self.trees:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.key > y.key:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order += 1
            aux[order] = x
        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if self.least is None or k.key < self.least.key:
                    self.least = k

    def decrease_key(self, x: FibonacciTree, new_key: float) -> None:
        """Decrease the key of node x to new_key."""
        if new_key > x.key:
            raise ValueError("New key is greater than current key")
        x.key = new_key
        y = x.parent
        if y is not None and x.key < y.key:
            self.cut(x, y)
            self.cascading_cut(y)
        if self.least is not None and x.key < self.least.key:
            self.least = x

    def cut(self, x: FibonacciTree, y: FibonacciTree) -> None:
        """Cut the link between x and its parent y."""
        y.children.remove(x)
        y.order -= 1
        x.parent = None
        x.marked = False
        self.trees.append(x)

    def cascading_cut(self, y: FibonacciTree) -> None:
        """Perform cascading cut operation starting from node y."""
        z = y.parent
        if z is not None:
            if not y.marked:
                y.marked = True
            else:
                self.cut(y, z)
                self.cascading_cut(z)

    def delete(self, x: FibonacciTree) -> None:
        """Delete node x from the heap."""
        self.decrease_key(x, float('-inf'))
        self.extract_min()



def floor_log2(x: int) -> int:
    """Return the floor of log2(x)."""
    return math.frexp(x)[1] - 1



if __name__ == "__main__":
    fheap = FibonacciHeap()
    fheap.insert(11)
    fheap.insert(10)
    fheap.insert(39)
    fheap.insert(26)
    fheap.insert(24)
    print(f"Minimum value: {fheap.get_min()}")
    print(f"Minimum value removed: {fheap.extract_min()}")
