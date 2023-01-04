class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


class SLinkedL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


    def insertSLL(self, value, location):
        newNode = Node(value)

        if self.head == None:
            self.head = newNode
            self.tail = newNode

        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode

            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1

                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode


    def traverseSSL(self):
        if self.head is None:
            print("The singly linked list does not exist ")

        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next


SinglyLinkedList = SLinkedL()
SinglyLinkedList.insertSLL(0, 0)
SinglyLinkedList.insertSLL(1, 0)
SinglyLinkedList.insertSLL(3, 0)
SinglyLinkedList.insertSLL(4, 0)
SinglyLinkedList.insertSLL(5, 0)

print([node.value for node in SinglyLinkedList])
SinglyLinkedList.traverseSSL()
