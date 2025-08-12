
"""
Queue implementation in Python.
"""

from typing import Any, List

class Queue:
    """
    A simple fixed-size queue implementation.
    """
    def __init__(self, k: int) -> None:
        """
        Initialize the queue with a fixed size k.
        """
        self.k: int = k
        self.queue: List[Any] = [None] * k
        self.head: int = -1
        self.tail: int = -1

    def enqueue(self, data: Any) -> None:
        """
        Insert an element into the queue.
        Prints a message if the queue is full.
        """
        if self.tail == self.k - 1:
            print("Queue is full")
        else:
            if self.head == -1:
                self.head = 0
            self.tail += 1
            self.queue[self.tail] = data
            print(f"Element {data} is inserted into the queue")

    def dequeue(self) -> Any:
        """
        Remove an element from the queue.
        Prints a message if the queue is empty.
        Returns the removed element or None.
        """
        if self.head == -1:
            print("Queue is empty")
            return None
        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = self.tail = -1
            print(f"Element {temp} is removed from the queue")
            return temp
        else:
            temp = self.queue[self.head]
            self.head += 1
            print(f"Element {temp} is removed from the queue")
            return temp

    def display(self) -> None:
        """
        Display the elements of the queue.
        Prints a message if the queue is empty.
        """
        if self.head == -1:
            print("Queue is empty")
        else:
            print("Queue elements are:")
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.display()
    q.dequeue()
    q.display()
    q.enqueue(6)
    q.display()
