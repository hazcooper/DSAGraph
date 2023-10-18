import numpy as np 
class DSAStack:

    def __init__(self, max_capacity=100):
        self.stack = np.empty(max_capacity,dtype = object) 
        self.count = 0
    
    def getCount(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.stack)

    def push(self, value):
        if not self.is_full():
            self.stack[self.count] = value
            self.count += 1
        else:
            raise ValueError("Stack is full")

    def pop(self):
        if not self.is_empty():
            self.count -= 1
            return self.stack[self.count]
        else:
            raise ValueError("Stack is empty")

    def top(self):
        if not self.is_empty():
            return self.stack[self.count - 1]
        else:
            raise ValueError("Stack is empty")






