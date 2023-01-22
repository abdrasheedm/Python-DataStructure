class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1


def peekofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]


def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        if rootNode.customList:
            for i in range(1, rootNode.heapSize + 1):
                print(rootNode.customList[i])
            return
        else:
            print("no heap")
            return


def heapifyTreeInsert(rootNode, index, heapType):
    parentIntex = int(index / 2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIntex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIntex]
            rootNode.customList[parentIntex] = temp
        heapifyTreeInsert(rootNode, index, heapType)

    if heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIntex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIntex]
            rootNode.customList[parentIntex] = temp
        heapifyTreeInsert(rootNode, parentIntex, heapType)


def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "heap is full"
    else:
        rootNode.customList[rootNode.heapSize + 1] = nodeValue
        rootNode.heapSize += 1
        heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
        return "The value succesfully inserted"


def heapifyExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = (index * 2) + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp

        else:
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heapifyExtract(rootNode, swapChild, heapType)


def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyExtract(rootNode, 1, heapType)
        return extractedNode


def deleteEntireBH(rootNode):
    rootNode.customList = None


newBinaryHeap = Heap(5)
insertNode(newBinaryHeap, 4, "Max")
insertNode(newBinaryHeap, 5, "Max")
insertNode(newBinaryHeap, 2, "Max")
insertNode(newBinaryHeap, 1, "Max")
# print(sizeofHeap(newBinaryHeap))
levelOrderTraversal(newBinaryHeap)
print("-------------------------------")
print(extractNode(newBinaryHeap, "Min"))
print('------------------')

levelOrderTraversal(newBinaryHeap)
print("-------------------------------")
print(extractNode(newBinaryHeap, "Max"))
print("-------------------------------")
deleteEntireBH(newBinaryHeap)
levelOrderTraversal(newBinaryHeap)