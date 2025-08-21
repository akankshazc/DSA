
"""
Insert a key into a B-tree in Python.
"""

from typing import List, Tuple, Optional

class BTreeNode:
    """
    A node in a B-tree.
    """
    def __init__(self, leaf: bool = False) -> None:
        """Initialize a B-tree node."""
        self.leaf: bool = leaf
        self.keys: List[Tuple] = []
        self.child: List['BTreeNode'] = []

class BTree:
    """
    B-tree with insertion and printing operations.
    """
    def __init__(self, t: int) -> None:
        """Initialize a B-tree with minimum degree t."""
        self.root: BTreeNode = BTreeNode(True)
        self.t: int = t

    def insert(self, k: Tuple) -> None:
        """Insert a key into the B-tree."""
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x: BTreeNode, k: Tuple) -> None:
        """Insert a key into a non-full node."""
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x: BTreeNode, i: int) -> None:
        """Split the child of node x at index i."""
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    def print_tree(self, x: Optional[BTreeNode], l: int = 0) -> None:
        """Print the B-tree structure level by level."""
        if x is None:
            return
        print(f"Level {l} {len(x.keys)}:", end=" ")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)


def main() -> None:
    B = BTree(3)
    for i in range(10):
        B.insert((i, 2 * i))
    B.print_tree(B.root)


if __name__ == '__main__':
    main()
