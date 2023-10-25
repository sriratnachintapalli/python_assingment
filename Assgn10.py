class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def __iter__(self):
        self.current_index = len(self.items) - 1
        return self

    def __next__(self):
        if self.current_index >= 0:
            value = self.items[self.current_index]
            self.current_index -= 1
            return value
        else:
            raise StopIteration

# Create a Stack instance
stack = Stack()

# Push some elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Use the iterator to pop elements in LIFO order
for item in stack:
    print("Popped:", item)

