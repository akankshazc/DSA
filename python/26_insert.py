
"""
Red-Black Tree insert implementation in Python.
Supports insert and traversal operations.
"""

import sys
from typing import Optional, Any

RED = 1
BLACK = 0

class Node:
    """
    Node of a Red-Black Tree.
    """
    def __init__(self, item: Any):
        self.item: Any = item
        self.parent: Optional['Node'] = None
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.color: int = RED



class RedBlackTree:
    """
    Red-Black Tree implementation supporting insert and traversal operations.
    """
    def __init__(self):
        self.TNULL: Node = Node(0)
        self.TNULL.color = BLACK
        self.TNULL.left = None
        self.TNULL.right = None
        self.root: Node = self.TNULL


    def pre_order_helper(self, node: Node) -> None:
        """
        Preorder traversal helper.
        """
        if node != self.TNULL:
            sys.stdout.write(str(node.item) + " ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)


    def in_order_helper(self, node: Node) -> None:
        """
        Inorder traversal helper.
        """
        if node != self.TNULL:
            self.in_order_helper(node.left)
            sys.stdout.write(str(node.item) + " ")
            self.in_order_helper(node.right)


    def post_order_helper(self, node: Node) -> None:
        """
        Postorder traversal helper.
        """
        if node != self.TNULL:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            sys.stdout.write(str(node.item) + " ")


    def search_tree_helper(self, node: Node, key: Any) -> Node:
        """
        Search for a key in the tree.
        """
        if node == self.TNULL or key == node.item:
            return node
        if key < node.item:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)


    def fix_insert(self, k: Node) -> None:
        """
        Balance the tree after insertion.
        """
        while k.parent.color == RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == RED:
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == RED:
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = BLACK


    def __print_helper(self, node: Node, indent: str, last: bool) -> None:
        """
        Print the tree structure.
        """
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            s_color = "RED" if node.color == RED else "BLACK"
            print(f"{node.item}({s_color})")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)


    def preorder(self) -> None:
        self.pre_order_helper(self.root)

    def inorder(self) -> None:
        self.in_order_helper(self.root)

    def postorder(self) -> None:
        self.post_order_helper(self.root)

    def searchTree(self, k: Any) -> Node:
        return self.search_tree_helper(self.root, k)

    def minimum(self, node: Node) -> Node:
        while node.left != self.TNULL:
            node = node.left
        return node

    def maximum(self, node: Node) -> Node:
        while node.right != self.TNULL:
            node = node.right
        return node

    def successor(self, x: Node) -> Node:
        if x.right != self.TNULL:
            return self.minimum(x.right)
        y = x.parent
        while y != self.TNULL and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, x: Node) -> Node:
        if x.left != self.TNULL:
            return self.maximum(x.left)
        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent
        return y

    def left_rotate(self, x: Node) -> None:
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x: Node) -> None:
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key: Any) -> None:
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = RED
        y = None
        x = self.root
        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node
        if node.parent is None:
            node.color = BLACK
            return
        if node.parent.parent is None:
            return
        self.fix_insert(node)

    def get_root(self) -> Node:
        return self.root

    def print_tree(self) -> None:
        self.__print_helper(self.root, "", True)


if __name__ == "__main__":
    bst = RedBlackTree()

    bst.insert(55)
    bst.insert(40)
    bst.insert(65)
    bst.insert(60)
    bst.insert(75)
    bst.insert(57)

    bst.print_tree()
