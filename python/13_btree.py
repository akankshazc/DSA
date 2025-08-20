
"""
Binary Tree implementation in Python.
"""

from typing import Optional


class Node:
    """
    A node in a binary tree.
    """

    def __init__(self, key: int) -> None:
        """Initialize a tree node with value and left/right children."""
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.val: int = key

    def traverse_preorder(self) -> None:
        """Preorder traversal (root, left, right)."""
        print(self.val, end=' ')
        if self.left:
            self.left.traverse_preorder()
        if self.right:
            self.right.traverse_preorder()

    def traverse_inorder(self) -> None:
        """Inorder traversal (left, root, right)."""
        if self.left:
            self.left.traverse_inorder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverse_inorder()

    def traverse_postorder(self) -> None:
        """Postorder traversal (left, right, root)."""
        if self.left:
            self.left.traverse_postorder()
        if self.right:
            self.right.traverse_postorder()
        print(self.val, end=' ')


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    print("Pre order Traversal: ", end="")
    root.traverse_preorder()
    print("\nIn order Traversal: ", end="")
    root.traverse_inorder()
    print("\nPost order Traversal: ", end="")
    root.traverse_postorder()
