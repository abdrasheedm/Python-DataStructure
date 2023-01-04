class Node:
    def __init__(self, value =None):
        self.value = value
        self.next = None


class SLink:
    def __init__(self):
        self.head = None
        self.tail = None

    # def __iter__(self):
    #     node = self.head
    #     while node:
    #         yield node
    #         node = node.next

    def insertSLL(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode

        else:
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode



    def list(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.next


    def remove_dup(self):
        node = self.head
        if node is None:
            print("No such linked list found ")
            return

        while node.next is not None:
            if node.value == node.next.value:
                new = node.next.next
                node.next = new
            else:
                node = node.next
        return "done"



array = [1, 2, 2, 3, 3, 4, 5]
SlinkedL = SLink()
for i in array:
    SlinkedL.insertSLL(i)

SlinkedL.list()

SlinkedL.remove_dup()
print("after removing duplicates")

SlinkedL.list()












