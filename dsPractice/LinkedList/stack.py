class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinikedL:
    def __init__(self):
        self.head = None
        self.tail = None


class Stack:
    def __init__(self):
        self.linkedList = LinikedL()

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        newnode = Node(value)

        if self.linkedList.head == None:
            self.linkedList.head = self.linkedList.tail = newnode
        else:
            newnode.next = self.linkedList.head
            self.linkedList.head = newnode

        return value

    def pop(self):
        if self.isEmpty():
            return "Stack is full"
        else:
            last = self.linkedList.head
            self.linkedList.head = self.linkedList.head.next

        return last.value


customStack = Stack()
print(customStack.isEmpty())
print(customStack.push(1))
print(customStack.pop())