# push/pop element = O(1)
# search element = O(n)
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

item = Stack()
item.push('harshad')
item.push('sam')
item.push('anfus')
item.push('sameeh')

print(item.pop())
print(item.peek())


