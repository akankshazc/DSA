
"""
Check if a binary tree is a complete binary tree in Python.
"""

from typing import Optional

class Node:
    """
    A node in a binary tree.
    """
    def __init__(self, item: int) -> None:
        """Initialize a tree node with value and left/right children."""
        self.item: int = item
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

def count_nodes(root: Optional[Node]) -> int:
    """
    Count the number of nodes in the binary tree rooted at 'root'.
    """
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def is_complete(root: Optional[Node], index: int, number_nodes: int) -> bool:
    """
    Check if the binary tree rooted at 'root' is a complete binary tree.
    """
    if root is None:
        return True
    if index >= number_nodes:
        return False
    return (is_complete(root.left, 2 * index + 1, number_nodes)
            and is_complete(root.right, 2 * index + 2, number_nodes))


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    node_count = count_nodes(root)
    index = 0
    if is_complete(root, index, node_count):
        print("The tree is a complete binary tree")
    else:
        print("The tree is not a complete binary tree")
