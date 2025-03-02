# Queue implementation in python

class Queue:

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the queue
    def enqueue(self, data):

        if self.tail == self.k - 1:
            print("Queue is full")
        else:
            if self.head == -1:
                self.head = 0
            self.tail += 1
            self.queue[self.tail] = data
            print(f"Element {data} is inserted into the queue")

    # Remove an element from the queue
    def dequeue(self):

        if self.head == -1:
            print("Queue is empty")

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

    # Display the queue
    def display(self):

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
