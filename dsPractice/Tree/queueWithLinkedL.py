
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
            # print(self.linkedList.head)

        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
            # print(self.tail)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"

        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = self.linkedList.tail = None

            else:
                self.linkedList.head = self.linkedList.head.next

            return tempNode

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.linkedList.head

    def delete(self):
        self.linkedList.head = self.linkedList.tail = None



customQueue = Queue()
print(customQueue.isEmpty())
print(customQueue.dequeue())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)

print(customQueue)
print('----------------')
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())
customQueue.delete()
print(customQueue, 'deleted')