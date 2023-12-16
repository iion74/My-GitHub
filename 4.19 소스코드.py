class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def push(self, item):
        if self.top == self.capacity - 1:
            return False  # Stack is full
        self.top += 1
        self.stack[self.top] = item
        return True

    def pop(self):
        if self.is_empty():
            return None  # Stack is empty
        item = self.stack[self.top]
        self.top -= 1
        return item

    def is_empty(self):
        return self.top == -1
