class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def top(self):
        self.items.reverse()
        print(self.items[0])

    
s = Stack()
print(s.is_empty())
s.push(5)
s.push(10)
s.push(30)
s.top()
s.pop()
s.top()
print(s.is_empty())
