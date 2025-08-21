"""
AVL tree implementation in Python.
"""

import sys
from typing import Optional


class TreeNode:
    """
    A node in an AVL tree.
    """

    def __init__(self, key: int) -> None:
        """Initialize a tree node with value, left/right children, and height."""
        self.key: int = key
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None
        self.height: int = 1


class AVLTree:
    """
    AVL tree with insertion and deletion operations.
    """

    def insert_node(self, root: Optional[TreeNode], key: int) -> TreeNode:
        """Insert a node with the given key into the AVL tree."""
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        balance_factor = self.get_balance(root)
        if balance_factor > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance_factor < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    def delete_node(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # Find the node to be deleted and remove it

        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)
        if root is None:
            return root
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        balance_factor = self.get_balance(root)
        if balance_factor > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance_factor < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    def left_rotate(self, z: TreeNode) -> TreeNode:
        """Perform left rotation on the subtree rooted at z."""
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z: TreeNode) -> TreeNode:
        """Perform right rotation on the subtree rooted at z."""
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root: Optional[TreeNode]) -> int:
        """Get the height of the node."""
        if not root:
            return 0
        return root.height

    def get_balance(self, root: Optional[TreeNode]) -> int:
        """Get the balance factor of the node."""
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Get the node with the minimum key value found in the tree."""
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def preorder(self, root: Optional[TreeNode]) -> None:
        """Preorder traversal of the AVL tree."""
        if not root:
            return
        print(f"{root.key} ", end="")
        self.preorder(root.left)
        self.preorder(root.right)

    def print_helper(self, curr_ptr: Optional[TreeNode], indent: str, last: bool) -> None:
        """Print the AVL tree structure."""
        if curr_ptr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(curr_ptr.key)
            self.print_helper(curr_ptr.left, indent, False)
            self.print_helper(curr_ptr.right, indent, True)


if __name__ == "__main__":
    my_tree = AVLTree()
    root = None
    nums = [33, 13, 52, 9, 21, 61, 8, 11]
    for num in nums:
        root = my_tree.insert_node(root, num)
    my_tree.print_helper(root, "", True)
    key = 13
    root = my_tree.delete_node(root, key)
    print("After Deletion: ")
    my_tree.print_helper(root, "", True)
