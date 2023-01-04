class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        self.list.reverse()
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return "Stack is full"
        else:
            self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return "The stack is Empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return " The Stack is empty"
        else:
            return self.list[len(self.list) -1]

    def delete(self):
        self.list = []


LimitedStack = Stack(5)
print(LimitedStack.isEmpty())
print("------------------")
print(LimitedStack.isFull())
print("------------------")
LimitedStack.push(1)
LimitedStack.push(2)
LimitedStack.push(3)
LimitedStack.push(4)
LimitedStack.push(5)
print(LimitedStack)
print("------------------")
print(LimitedStack.push(5))
print(LimitedStack.peek())
LimitedStack.delete()
print("------------------")
print(LimitedStack, 'hai')
