import numpy as np
class DSAQueue:
    def __init__(self, max_capacity=100):
        self.queue = np.empty(max_capacity,dtype = object)
        self.front = 0
        self.rear = -1
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.queue)

    def enqueue(self, item):
        if not self.is_full():
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = item
            self.count += 1
        else:
            raise ValueError("Queue is full")

    def dequeue(self):
        if not self.is_empty():
            front_item = self.queue[self.front]
            self.front += 1
            self.count -= 1
            return front_item
        else:
            raise ValueError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.queue[self.front]
        else:
            raise ValueError("Queue is empty")


