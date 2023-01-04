class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        self.list.reverse()
        return ' '.join(values)

    #isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    #Push
    def push(self, value):
        self.list.append(value)
        return "Value added"

    #Pop
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list.pop()

    #Peek
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list[len(self.list) - 1]

    #delete
    def delete(self):
        self.list = None

stack = Stack()
print(stack.isEmpty())

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack)
print("------------------")

print(stack.pop())
# print("------------------")
# print(stack)
# print("------------------")
# print(stack.peek())



