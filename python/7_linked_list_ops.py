
"""
Linked list operations in Python.
"""

from typing import Any, Optional


class Node:
    """
    A node in a singly linked list.
    """

    def __init__(self, data: Any) -> None:
        """Initialize a node with data and next pointer."""
        self.data: Any = data
        self.next: Optional['Node'] = None


class LinkedList:
    """
    A simple singly linked list with basic operations.
    """

    def __init__(self) -> None:
        """Initialize an empty linked list."""
        self.head: Optional[Node] = None

    def insert_at_beginning(self, new_data: Any) -> None:
        """Insert a new node at the beginning of the list."""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node: Optional[Node], new_data: Any) -> None:
        """Insert a new node after the given previous node."""
        if prev_node is None:
            print("The given previous node must be in the LinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_at_end(self, new_data: Any) -> None:
        """Insert a new node at the end of the list."""
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, position: int) -> None:
        """Delete the node at the given position (0-based index)."""
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for _ in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None or temp.next is None:
            return

        next_node = temp.next.next

        temp.next = None
        temp.next = next_node

    def search(self, key: Any) -> bool:
        """Search for an element in the linked list."""
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def sort_linked_list(self, head: Optional[Node]) -> None:
        """Sort the linked list using bubble sort (in-place)."""
        current = head
        if head is None:
            return
        while current is not None:
            index = current.next
            while index is not None:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next

    def print_list(self) -> None:
        """Print the elements of the linked list."""
        temp = self.head
        while temp:
            print(f"{temp.data} ", end="")
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_at_end(1)
    llist.insert_at_beginning(2)
    llist.insert_at_beginning(3)
    llist.insert_at_end(4)
    llist.insert_after(llist.head.next, 5)
    print('Linked list:')
    llist.print_list()
    print("\nAfter deleting an element:")
    llist.delete_node(3)
    llist.print_list()
    print()
    item_to_find = 3
    if llist.search(item_to_find):
        print(f"{item_to_find} is found")
    else:
        print(f"{item_to_find} is not found")
    llist.sort_linked_list(llist.head)
    print("Sorted list:")
    llist.print_list()
