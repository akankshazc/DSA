
"""
Check if a binary tree is a full binary tree in Python.
"""

from typing import Optional

class Node:
    """
    A node in a binary tree.
    """
    def __init__(self, item: int) -> None:
        """Initialize a tree node with value and left/right children."""
        self.item: int = item
        self.leftChild: Optional['Node'] = None
        self.rightChild: Optional['Node'] = None

def is_full_tree(root: Optional[Node]) -> bool:
    """
    Check if the binary tree rooted at 'root' is a full binary tree.
    """
    if root is None:
        return True
    if root.leftChild is None and root.rightChild is None:
        return True
    if root.leftChild is not None and root.rightChild is not None:
        return is_full_tree(root.leftChild) and is_full_tree(root.rightChild)
    return False


if __name__ == "__main__":
    root = Node(1)
    root.rightChild = Node(3)
    root.leftChild = Node(2)
    root.leftChild.leftChild = Node(4)
    root.leftChild.rightChild = Node(5)
    root.leftChild.rightChild.leftChild = Node(6)
    root.leftChild.rightChild.rightChild = Node(7)
    if is_full_tree(root):
        print("The tree is a full binary tree")
    else:
        print("The tree is not a full binary tree")
