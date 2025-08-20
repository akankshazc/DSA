
"""
Tree traversal in Python.
"""

from typing import Optional


class Node:
    """
    A node in a binary tree.
    """

    def __init__(self, item: int) -> None:
        """Initialize a tree node with value and left/right children."""
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.val: int = item


def inorder(root: Optional[Node]) -> None:
    """Inorder tree traversal (left, root, right)."""
    if root:
        inorder(root.left)
        print(f"{root.val}->", end='')
        inorder(root.right)


def postorder(root: Optional[Node]) -> None:
    """Postorder tree traversal (left, right, root)."""
    if root:
        postorder(root.left)
        postorder(root.right)
        print(f"{root.val}->", end='')


def preorder(root: Optional[Node]) -> None:
    """Preorder tree traversal (root, left, right)."""
    if root:
        print(f"{root.val}->", end='')
        preorder(root.left)
        preorder(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Inorder traversal ")
    inorder(root)
    print("\nPreorder traversal ")
    preorder(root)
    print("\nPostorder traversal ")
    postorder(root)
