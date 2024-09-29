# Array implementation
class Array:
    def __init__(self):
        self.array = []
    
    def insert(self, index, value):
        self.array.insert(index, value)
    
    def delete(self, index):
        self.array.pop(index)
    
    def access(self, index):
        return self.array[index]

# Stack using Array
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def is_empty(self):
        return len(self.stack) == 0

# Queue using Array
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None
    
    def is_empty(self):
        return len(self.queue) == 0

# Singly Linked List implementation
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, value):
        prev = None
        curr = self.head
        while curr:
            if curr.value == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False
    
    def traverse(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.value)
            curr = curr.next
        return elements
