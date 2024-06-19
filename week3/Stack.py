class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def pop(self):
        if self.is_empty():
            print("pop from empty stack")
        return self.stack.pop()

    def push(self, value):
        if self.is_full():
            print("push to full stack")
        self.stack.append(value)

    def top(self):
        if self.is_empty():
            print("top from empty stack")
        return self.stack[-1]


stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
