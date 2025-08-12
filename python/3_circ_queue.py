
"""
Circular Queue Implementation in Python.
"""

from typing import Any, List

class MyCircularQueue:
    """
    A simple circular queue implementation.
    """
    def __init__(self, k: int) -> None:
        """
        Initialize the circular queue with a fixed size k.
        """
        self.k: int = k
        self.queue: List[Any] = [None] * k
        self.head: int = -1
        self.tail: int = -1

    def enqueue(self, data: Any) -> None:
        """
        Insert an element into the circular queue.
        Prints a message if the queue is full.
        """
        if (self.tail + 1) % self.k == self.head:
            print("The circular queue is full\n")
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    def dequeue(self) -> Any:
        """
        Delete an element from the circular queue.
        Prints a message if the queue is empty.
        Returns the removed element or None.
        """
        if self.head == -1:
            print("The circular queue is empty\n")
            return None
        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCQueue(self) -> None:
        """
        Display the elements of the circular queue.
        Prints a message if the queue is empty.
        """
        if self.head == -1:
            print("No element in the circular queue")
        elif self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


if __name__ == "__main__":
    obj = MyCircularQueue(5)
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.enqueue(4)
    obj.enqueue(5)
    print("Initial queue")
    obj.printCQueue()

    obj.dequeue()
    print("After removing an element from the queue")
    obj.printCQueue()
