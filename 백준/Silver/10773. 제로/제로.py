class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)

        if self.top is None:
            self.top = new_node
        else:
            current = new_node
            current.next = self.top
            self.top = current
    
    def pop(self):
        if self.top is None:
            return False
        else:
            self.top = self.top.next

    def add(self):
        total = 0
        while self.top:
            total += self.top.data
            self.top = self.top.next
        return total


repeat = int(input())
ex = Stack()
for _ in range (0, repeat):
    a = int(input())
    if a != 0:
        ex.push(a)
    elif a == 0:
        ex.pop()

print(ex.add())
        

    