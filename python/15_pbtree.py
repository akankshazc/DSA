
"""
Check if a binary tree is a perfect binary tree in Python.
"""

from typing import Optional

class Node:
    """
    A node in a binary tree.
    """
    def __init__(self, key: int) -> None:
        """Initialize a tree node with value and left/right children."""
        self.key: int = key
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

def calculate_depth(node: Optional[Node]) -> int:
    """
    Calculate the depth of the binary tree rooted at 'node'.
    """
    if node is None:
        return 0
    left_depth = calculate_depth(node.left)
    right_depth = calculate_depth(node.right)
    return max(left_depth, right_depth) + 1

def is_perfect(root: Optional[Node], d: int, level: int = 0) -> bool:
    """
    Check if the binary tree rooted at 'root' is a perfect binary tree.
    """
    if root is None:
        return True
    if root.left is None and root.right is None:
        return d == level + 1
    if root.left is None or root.right is None:
        return False
    return is_perfect(root.left, d, level + 1) and is_perfect(root.right, d, level + 1)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    if is_perfect(root, calculate_depth(root)):
        print("The tree is a perfect binary tree")
    else:
        print("The tree is not a perfect binary tree")
