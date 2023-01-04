class Queue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.items = maxSize * [None]
        self.start = -1
        self.top = -1

    def __str__(self):
        values = (str(x) for x in self.items)
        return " ".join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif (self.start == 0 and self.top == self.maxSize - 1):
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == - 1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            return "The queue is Full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == - 1:
                    self.start = 0

            self.items[self.top] = value
            return "value added"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            firstValue = self.items[self.start]
            start = self.start

            if self.start + 1 == self.maxSize:
                self.start = 0
            elif self.start == self.top:
                self.start = -1
                self.top = -1
            else:
                self.start += 1

            self.items[start] = None
            return firstValue

    def peek(self):
        if self.isEmpty():
            return "Que is empty"
        else:
            return self.items[self.start]

    def delete(self):
        self.start = - 1
        self.top = -1




customQueue = Queue(5)


customQueue.enqueue(1)
customQueue.enqueue(2)
print(customQueue.enqueue(3))
customQueue.enqueue(4)
customQueue.enqueue(5)

print(customQueue)
print("-------------------")
print(customQueue.dequeue())
print("-------------------")
print(customQueue)
print(customQueue.isFull())
print(customQueue.peek())
customQueue.delete()
print(customQueue )

