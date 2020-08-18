#!/usr/bin/env python 3

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)



s = Stack()
s.push(10)
s.push(11)
s.push("cat")
s.push(12)
print(s.size())
print(s.peek())

