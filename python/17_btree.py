
"""
Check if a binary tree is height balanced in Python.
"""

from typing import Optional

class Node:
    """
    A node in a binary tree.
    """
    def __init__(self, data: int) -> None:
        """Initialize a tree node with value and left/right children."""
        self.data: int = data
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

class Height:
    """
    Helper class to store height value for recursive calls.
    """
    def __init__(self) -> None:
        self.height: int = 0

def is_height_balanced(root: Optional[Node], height: Height) -> bool:
    """
    Check if the binary tree rooted at 'root' is height balanced.
    """
    left_height = Height()
    right_height = Height()
    if root is None:
        return True
    l = is_height_balanced(root.left, left_height)
    r = is_height_balanced(root.right, right_height)
    height.height = max(left_height.height, right_height.height) + 1
    if abs(left_height.height - right_height.height) <= 1:
        return l and r
    return False


if __name__ == "__main__":
    height = Height()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    if is_height_balanced(root, height):
        print('The tree is balanced')
    else:
        print('The tree is not balanced')
