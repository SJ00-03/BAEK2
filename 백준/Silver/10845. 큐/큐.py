class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt = 0

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = new_node
            self.tail.next = current
            self.tail = current
        self.cnt += 1
    
    def empty(self):
        return self.head is None
    
    def pop(self):
        if self.empty():
            self.cnt = 0
            return -1
        current = self.head
        self.head = current.next
        self.cnt -= 1
        return current.data
    
    def size(self):
        return self.cnt
    
    def front(self):
        return -1 if self.empty() else self.head.data
    
    def back(self):
        return -1 if self.empty() else self.tail.data
    
repeat = int(input())
q = Queue()
for _ in range (0, repeat):
    a = input()
    parts = a.split()
    if parts[0] == "push":
        q.push(int(parts[1]))

    elif parts[0] == "empty":
        if q.empty():
            print("1")
        else:
            print("0")
       
    elif parts[0] == "pop":
        print(q.pop())
    elif parts[0] == "size":
        print(q.size())
    elif parts[0] == "front":
        print(q.front())
    elif parts[0] == "back":
        print(q.back())
    


