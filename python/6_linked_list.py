
"""
Linked list implementation in Python.
"""

from typing import Any, Optional

class Node:
    """
    A node in a singly linked list.
    """
    def __init__(self, item: Any) -> None:
        """
        Initialize a node with an item and next pointer.
        """
        self.item: Any = item
        self.next: Optional['Node'] = None

class LinkedList:
    """
    A simple singly linked list.
    """
    def __init__(self) -> None:
        """
        Initialize an empty linked list.
        """
        self.head: Optional[Node] = None


if __name__ == '__main__':
    linked_list = LinkedList()
    # Assign item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    # Connect nodes
    linked_list.head.next = second
    second.next = third
    # Print the linked list items
    current = linked_list.head
    while current is not None:
        print(current.item, end=" ")
        current = current.next
