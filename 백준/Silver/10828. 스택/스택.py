class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = new_node
            current.next = self.head
            self.head = current
    
    def pop(self):
        if self.head is None:
            print("-1")
        else:
            current = self.head
            print(f"{self.head.data}")
            self.head = current.next        
        
    def size(self):
        i = 0
        current = self.head
        while current:
            i += 1
            current = current.next
        print(f"{i}")
    
    def empty(self):
        if self.head is None:
            print("1")
            return True
            
        else:
            print("0")
            return False            
        
    def top(self):
        if self.head is None:
            print("-1")
            
        else:
            print(f"{self.head.data}")

repeat = int(input())
order = Stack()

for _ in range (0, repeat):
    
    a = input()
    parts = a.split()
    
    if parts[0] == "pop":
        order.pop()
    
    elif parts[0] == "size":
        order.size()
    
    elif parts[0] == "empty":
        order.empty()
    
    elif parts[0] == "top":
        order.top()
    
    elif parts[0] == "push":
        number = int(parts[1])
        order.push(number)


