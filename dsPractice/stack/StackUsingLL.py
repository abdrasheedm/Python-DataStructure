class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Stack:
    def __init__(self):
        self.LinkedL = LinkedList()

    def isEmpty(self):
        if self.LinkedL.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedL.head
        self.LinkedL.head = node

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            nodeValue = self.LinkedL.head.value
            self.LinkedL.head = self.LinkedL.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.LinkedL.head.value

    def delete(self):
        self.LinkedL.head = None


customStack = Stack()
print(customStack.isEmpty())

customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)

print([node.value for node in customStack.LinkedL])
print('-----------------------')
print(customStack.pop())
print('-----------------------')
print([node.value for node in customStack.LinkedL])
print('-----------------------')
print(customStack.peek())
print('-----------------------')
customStack.delete()
print([node.value for node in customStack.LinkedL])





