class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkdedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def InsertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
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
                index = 1
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


    def deleteNode(self, location):
        if self.head is None:
            print("No such Linkedlist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None

                else:
                    self.head = self.head.next

            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None

                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node

            else:
                tempNode = self.head
                index = 1
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1

                nextNode = tempNode.next
                tempNode.next = nextNode.next





SinglyLinkedList = SLinkdedList()
SinglyLinkedList.InsertSLL(0, 0)
SinglyLinkedList.InsertSLL(1, 0)
SinglyLinkedList.InsertSLL(3, 0)
SinglyLinkedList.InsertSLL(4, 0)
SinglyLinkedList.InsertSLL(5, 0)

print([node.value for node in SinglyLinkedList])
print(SinglyLinkedList.deleteNode(3))
print([node.value for node in SinglyLinkedList])

